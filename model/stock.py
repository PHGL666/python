from model.article import *
from model.stock_entry import StockEntry
from application import db

class Stock:
    def entries(self):
        return StockEntry.query.all()

    def addArticleQuantity(self, article, quantity):
        entry = StockEntry(article=article, quantity=quantity)
        db.session.add(entry)
        db.session.commit()

    def addStockEntry(self, entry):
        self.entries.append(entry)

    def print(self):
        print('************************')
        totalPrice = 0
        for entry in self.entries():
            print(entry.toString())
            totalPrice += entry.price()
        print('Total stock : {}€'.format(totalPrice))
        print('************************')

    def addArticle(self):
        article = Article.createArticle() #puiseque cest une méthode de class qu'il récupère je met un A majuscule a Article
        quantity = int(input("Quantité de l'article : "))
        # on utilise la méthode addArticleQuantity ci-dessus pour importer notre article nouvellement instancier dans le stock
        self.addArticleQuantity(article, quantity)

stock = Stock()
# stock.addArticleQuantity(article, 1)
# stock.addArticleQuantity(article2, 10)
# stock.addArticleQuantity(article3, 20)
# stock.print()
