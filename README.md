# Framework FLASK

https://flask.palletsprojects.com/en/1.1.x/installation/

> LANCER WAMP SERVER

## Préparer l'environnement virtuel
Il faut un environnement virtuel (venv) pour encapsuler python et flask.
```
py -3 -m venv venv
```

puis il faut activer l'environnement. Pour ce faire dans le dossier TEST-FLASK terminal taper
venv\Scripts\activate

on est maintenant dans le venv.

## Installation de Flask
```
pip install Flask
```
fin

création du fichier application.py
```
from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello, World !'


@app.route('/user/<username>/<other>')
def show_username(username, other):
    return 'Hello, {}, {}'.format(username, other)
```


https://flask.palletsprojects.com/en/1.1.x/quickstart/

> Pour lancer l'application
```
$env:FLASK_APP = "application.py"
```
puis 
```
flask run
```

test avec l'url
http://127.0.0.1:5000/hello
http://127.0.0.1:5000/user/name/test


on va poser des contraintes, par exemple on va restreindre other en int:
```
@app.route('/user/<username>/<int:other>')
```

## Moteur de rendu de template JINJA2

>création du dossiers templates qui contiendra nos vues et on y crée le fichier index.html
dans application.py on fait l'imprt de Jinja et on rajoute une route pour notre page d'accueil
```
from flask import render_template # Jinja2
```

```
@app.route('/')
def index():
    return render_template('index.html', liste = ['Item 1', 'Item 2', 'Item 3'])
```

## INSTALLATION BOOTSTRAP
https://pythonhosted.org/Flask-Bootstrap/
```
pip install flask-bootstrap
```

## INSTALLATION DE SQLALCHEMY 

dans venv
```
venv\Scripts\activate
```

```
$env:FLASK_APP = "application.py"
```

```
pip install Flask-SQLAlchemy
```

```
flask run
```

dans fichier application.py on rajoute les lignes suivantes :
> on donne le chemin
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
```
> on appelle la base de donnée
```
db = SQLAlchemy(app)
```

### MISE A JOUR FICHIER ARTICLE.PY

dans article.py on import notre db
```
import application import db
```
et on met à jour la class et on 
```
class Article(db.Model):
```
> OBS : 
1ier int entrée qui n'est
pas une foreign key et qui est une
primary key
=> sera avec python la prmeière ID QUI S'AUTOINCREMENTE

on met à jour la table de données avec les variables suivantes
```
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)
```

on peut dès lors supprimer le constructeur qui n'est plus utile
```
    def __init__(self, name, description, price):
        Article.currentId += 1
        self.id = Article.currentId
        self.name = name
        self.description = description
        self.price = price
```
> en effet db.Model se basera sur les variables créer pour lui même créer un constructeur automatiquement. 

et on commente tous les articles en bas pour pas qu'il s'incrémente à chaque lancement de serveur puisqu'il y a dorénavant la persistence des données.

de même on comment tous les articles en bas dans le fichier stock.py

### MISE A JOUR FICHIER STOCK_ENTRY.PY

mise à jour des imports
```
from model.article import db
from application import db
```

mise à jour de la class
```
class StockEntry(db.Model):
```

puis on ajoute les liens
```
article_id = db.Column(db.Integer, db.ForeignKey('article.id'), primary_key=True, nullable=False)
```

### MISE A JOUR FICHIER STOCK.PY

c'est la class Stock qui va faire les requêtes en base de données. 

mise à jour des imports
```
from model.article import *
from model.stock_entry import StockEntry
from application import db
```

mise à jour de la class
```
class Stock:
    def entries(self):
        return StockEntry.query.all()
```
> OBS : il n'est pas utilise de mettre Stock en base de donnée donc on n'ajoute pas db.Model.

```
    def addArticleQuantity(self, article, quantity):
    entry = StockEntry(article=article, quantity=quantity)
    db.session.add(entry)
    db.session.commit()
```
> le db.session permet d'appliquer les modifications sur la base de données

ajout des parenthèses au entries dans le print pour pouvoir appeler la fonction entries
```
    def print(self):
        print('************************')
        totalPrice = 0
        for entry in self.entries():
            print(entry.toString())
            totalPrice += entry.price()
        print('Total stock : {}€'.format(totalPrice))
        print('************************')
```

dans APPLICATION.PY mise à jour des routes
```
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


@app.route('/')
def index():
    return render_template('index.html', entries=stock.entries())
```

dans application.py mise à jour de l'ordre des imports
```
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
```

# DANS LE SHELL DE FLASK

taper
```
flask shell
```

```
from application import db
```

on utilise une méthode de sqlalchemy pour créer le schéma de la bd
```
db.create_all()
```

un fichier data.db a été crée dans notre environnement.

> pour lire ce fihier nous allons installer un logiciel 
https://sqlitebrowser.org/dl/


### COMMENT RECUPERER UN OBJET DE PAR SON ID

Get Model by value:
```
entry = StockEntry.query.filter_by(article_id=xx).first()
article = StockEntry.query.filter_by(id=xx).first()
```

### AJOUTER UNE SUPRRESSION

```
# entry = StockEntry.query.filter_by(article_id=xx).first()
# article = StockEntry.query.filter_by(id=xx).first()

# db.session.delete(entry)
# db.session.delete(article)
# db.session.commit()
```

dans l'index.html
```
<button href="/delete_article/{{ entry.article.id }}" class="btn btn-danger">Supprimer</button>
```

dans application on crée la route de suppression
```
@app.route('/delete_article/<int:article_id>')
    def deleteArticle(article_id):
```

dans stock.py
```
    def deleteArticleById(self, article_id):
        entry = StockEntry.query.filter_by(article_id=article_id).first()
        article = Article.query.filter_by(id=article_id).first()
        db.session.delete(entry)
        db.session.delete(article)
        db.session.commit()
```

dans application.py
```

```