from flask import Flask
from flask import render_template  # Jinja2
from flask import request
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

from model.stock import stock
from model.article import Article


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<username>/<int:other>')
def show_username(username, other):
    return 'Hello, {}, {}'.format(username, other)

@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    if request.method == 'GET':
        return render_template('add_article.html')
    else:
        articleName = request.form['name']
        articleDescription = request.form['description']
        articlePrice = request.form['price']

        article = Article(name=articleName, description=articleDescription, price=int(articlePrice))
        stock.addArticleQuantity(article, 1)

        return redirect(url_for('index'))

@app.route('/delete_article/<int:article_id>')
def deleteArticle(article_id):
    stock.deleteArticleById(article_id)
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', entries=stock.entries())