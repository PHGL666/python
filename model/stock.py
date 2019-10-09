from article import *
from stock_entry import StockEntry

class Stock:
    def __init__(self):
        self.entries = []

    def addArticleQuantity(self, article, quantity):
        entry = StockEntry(article, quantity)
        self.entries.append(entry)

    def addStockEntry(self, entry):
        self.entries.append(entry)

    def print(self):
        print('************************')
        totalPrice = 0
        for entry in self.entries:
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
stock.addArticleQuantity(article, 1)
stock.addArticleQuantity(article2, 10)
stock.addArticleQuantity(article3, 20)
# stock.print()
