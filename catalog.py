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


if __name__ == '__main__':
  app.secret_key = 'secret_catalog_app'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)