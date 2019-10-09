from article import Article

class StockEntry:
    def __init__(self, article, quantity):
        self.article = article
        self.quantity = quantity

    def price(self):
        return self.article.price * self.quantity

    def toString(self):
        return '{} x {}'.format(self.article.toString(), self.quantity)