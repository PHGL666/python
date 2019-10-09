import application import db

class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, name, description, price):
        Article.currentId += 1
        self.id = Article.currentId
        self.name = name
        self.description = description
        self.price = price

    def print(self):
        print('[{}] Article {} - {}€ : \n{}'.format(self.id, self.name, self.price, self.description))

    def toString(self):
        return '{} - {}€'.format(self.name, self.price)

    # création de la methode pour créer un article. une fois fait on va dans stock pour récupérer un article creer par un utilissateur avec addArticle
    @classmethod
    def createArticle(cls):
        name = input("Nom de l'article : ")
        description = input("Description de l'article : ")
        price = int(input("Prix de l'article : "))
        article = Article(name, description, price)
        return article

article = Article('Macbook', 'Ordinateur Apple', 1500)
# article.print()

article2 = Article('Article2', 'Description2', 300)
# article2.print()

article3 = Article('Article3', 'Description 3', 100)
# article3.print()
