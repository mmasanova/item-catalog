from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

# Connect to Database and create database session
engine = create_engine('sqlite:///item_catalog.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/catalog')
def showCatalog():
	category_id = 1
	categories = session.query(Category).order_by(asc(Category.name)).all()
	items = session.query(Item).filter_by(category_id = category_id).all()
	return render_template('catalog.html', category_id = category_id, categories = categories, items = items)

@app.route('/category/<int:category_id>', methods=['GET', 'POST'])
def showCategory(category_id):
	category = session.query(Category).filter_by(id = category_id).one()
	items = session.query(Item).filter_by(category_id = category_id).all()
	return render_template('category.html', category = category, items = items)

@app.route('/category/add', methods=['GET', 'POST'])
def addCategory():
	if request.method == 'POST':
		if (request.form['name']):
			category = Category(name = request.form['name'], user_id = 1)
			session.add(category)
			session.commit()
			return redirect(url_for('showCatalog'))
		else:
			flash('Category name is required')
			return render_template('catalog')
	else:
		return render_template('addCategory.html')

@app.route('/category/<int:category_id>/edit', methods=['POST', 'GET'])
def editCategory(category_id):
	category = session.query(Category).filter_by(id = category_id).one()

	if request.method == 'POST':
		category.name = request.form['name']
		session.add(category)
		session.commit()
		return redirect(url_for('showCatalog'))
	else:
		return render_template('editCategory.html', category = category)

@app.route('/category/<int:category_id>/delete', methods=['POST', 'GET'])
def deleteCategory(category_id):
	category = session.query(Category).filter_by(id = category_id).one()

	if request.method == 'POST':
		session.delete(category)
		session.commit()
		return redirect(url_for('showCatalog'))
	else:
		return render_template('deleteCategory.html', category = category)

@app.route('/category/<int:category_id>/item/<int:item_id>', methods=['POST', 'GET'])
def showItem(category_id, item_id):
	category = session.query(Category).filter_by(id = category_id).one()
	item = session.query(Item).filter_by(id = item_id).one()
	return render_template('item.html', category = category, item = item)

@app.route('/category/<int:category_id>/item/add', methods=['POST', 'GET'])
def addItem(category_id):
	if request.method == 'POST':
		if (request.form['name']):
			item = Item(name = request.form['name'], description = request.form['description'],
				long_description = request.form['long_description'], user_id = 1, category_id = category_id)
			session.add(item)
			session.commit()
			return redirect(url_for('showCategory', category_id = category_id))
		else:
			flash('Item name is required.')
			return redirect(url_for('addItem', category_id = category_id))
	else:
		category = session.query(Category).filter_by(id = category_id).one()
		return render_template('addItem.html', category = category)

@app.route('/category/<int:category_id>/item/<int:item_id>/edit', methods=['POST', 'GET'])
def editItem(category_id, item_id):
	category = session.query(Category).filter_by(id = category_id).one()
	item = session.query(Item).filter_by(id = item_id).one()

	if request.method == 'POST':
		item.name = request.form['name']
		item.description = request.form['description']
		item.long_description = request.form['long_description']
		session.add(item)
		session.commit()
		return redirect(url_for('showItem', category_id = category_id, item_id = item_id))
	else:
		return render_template('editItem.html', category = category, item = item)

@app.route('/category/<int:category_id>/item/<int:item_id>/delete', methods=['POST', 'GET'])
def deleteItem(category_id, item_id):
	category = session.query(Category).filter_by(id = category_id).one()
	item = session.query(Item).filter_by(id = item_id).one()

	if request.method == 'POST':
		session.delete(item)
		session.commit()
		return redirect(url_for('showItem', category_id = category_id, item_id = item_id))
	else:
		return render_template('deleteItem.html', category = category, item = item)

# JSON API endpoint to view all categories
@app.route('/categories/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[c.serialize for c in categories])

# JSON API endpoint to view a single category
@app.route('/category/<int:category_id>/JSON')
def categoryJSON(category_id):
	category = session.query(Category).filter_by(id = category_id).one()
	return jsonify(category = category.serialize)

# JSON API endpoint to view category items
@app.route('/category/<int:category_id>/items/JSON')
def itemsJSON(category_id):
	items = session.query(Item).filter_by(category_id = category_id).all()
	return jsonify(items = [i.serialize for i in items])

# JSON API endpoint to view a category item
@app.route('/category/<int:category_id>/items/<int:item_id>/JSON')
def categoryItemJSON(category_id, item_id):
	item = session.query(Item).filter_by(category_id = category_id).filter_by(id = item_id).one()
	return jsonify(item = item.serialize)

# JSON API endpoint to view an arbitrary item based on id
@app.route('/item/<int:item_id>/JSON')
def itemJSON(item_id):
	item = session.query(Item).filter_by(id = item_id).one()
	return jsonify(item = item.serialize)

if __name__ == '__main__':
  app.secret_key = 'secret_catalog_app'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)