from flask import Flask
from flask_mongoengine import BaseQuerySet
from mongoengine import Document, StringField, IntField, EmbeddedDocument, EmbeddedDocumentField
from dataclasses import dataclass
from .. import db
import json

@dataclass
class Product(db.Document):
    """ Product Model for storing Product related details """
    id:int
    name:str
    description:str
    imagename:str
    meta = {'collection': 'products',  'queryset_class': BaseQuerySet}

    id = db.IntField(primary_key=True)
    name = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255, required=True)
    producttype_id = db.IntField()
    imagename =db.StringField(max_length=255, required=True)

    #__tablename__ = "products"
    #id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #name = db.Column(db.String(255), unique=True, nullable=False)
    #description = db.Column(db.String(255), unique=True, nullable=False)
    #producttype_id = db.Column(db.Integer, db.ForeignKey('product_types.id'))
    #producttype =  db.relationship('ProductType', backref='Product', lazy=True)
    #imagename = db.Column(db.String(255), unique=True, nullable=True)

    def __init__(self, id, name, description, producttypeid, imagename,*args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.id = id
        self.name = name
        self.description = description
        self.producttype_id=producttypeid
        self.imagename=imagename

    def __repr__(self):
        return "<Product '{}'>".format(self.name)

    def to_json(self):
        return "{ id:" + str(self.id) + ", name:" + self.name +",description:" + self.description + "}"

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
