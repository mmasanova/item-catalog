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

@app.route('/category/add', methods=['GET', 'POST'])
def addCategory():
	if request.method == 'POST':
		category = Category(name = request.form['name'], user_id = 1)
		session.add(category)
		session.commit()
		return redirect(url_for('showCatalog'))
	else:
		return render_template('addCategory.html')

@app.route('/category/<int:category_id>/item/add', methods=['POST','GET'])
def addItem(category_id):
	if request.method == 'POST':
		item = Item(name = request.form['name'], description = request.form['description'],
			long_description = request.form['long_description'], user_id = 1, category_id = category_id)
		session.add(item)
		session.commit()
		return redirect(url_for('showCatalog'))
	else:
		return render_template('addItem.html', category_id = category_id)

if __name__ == '__main__':
  app.secret_key = 'secret_catalog_app'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)