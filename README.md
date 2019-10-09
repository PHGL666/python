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

dans article.py on import notre db
```
import application import db
```
et on met à jour la class et on 
```
class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True)
```
> OBS : 
1ier int entrée qui n'est
pas une foreign key et qui est une
primary key
=> sera avec python la prmeière ID QUI SINCREMENTE AUTOMATIQUEMENT


