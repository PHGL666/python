from model.article import db
from application import db


class StockEntry(db.Model):

    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), primary_key=True, nullable=False)
    article = db.relationship('Article')

    quantity = db.Column(db.Integer, default=0)

    def __init__(self, article, quantity):
        self.article = article
        self.quantity = quantity

    def price(self):
        return self.article.price * self.quantity

    def toString(self):
        return '{} x {}'.format(self.article.toString(), self.quantity)