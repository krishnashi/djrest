from enum import unique

from fiveproj import db

class ItemsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False, unique=True)
