from model.article import  *
from model.stock_entry import StockEntry
from application import db

class Stock:
    def entries(self):
        return StockEntry.query.all()

    def addArticleQuantity(self, article, quantity):
        entry = StockEntry(article=article, quantity=quantity)
        db.session.add(entry)
        db.session.commit()

    def deleteArticleById(self, article_id):
        entry = StockEntry.query.filter_by(article_id=article_id).first()
        article = Article.query.filter_by(id=article_id).first()
        db.session.delete(entry)
        db.session.delete(article)
        db.session.commit()

    def addStockEntry(self, entry):
        db.session.add(entry)
        db.session.commit()

    def print(self):
        print('************************')
        totalPrice = 0
        for entry in self.entries():
            print(entry.toString())
            totalPrice += entry.price()
        print('Total stock : {}€'.format(totalPrice))
        print('************************')
    
    def addArticle(self):
        article = Article.createArticle()
        quantity = int(input("Quantité de l'article : "))
        self.addArticleQuantity(article, quantity)

stock = Stock()
#stock.addArticleQuantity(article, 1)
#stock.addArticleQuantity(article2, 10)
#stock.addArticleQuantity(article3, 20)
#stock.print()