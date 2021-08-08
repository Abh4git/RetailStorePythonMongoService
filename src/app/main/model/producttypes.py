from flask import Flask
from mongoengine import Document, StringField, IntField, EmbeddedDocument, EmbeddedDocumentField
from flask_mongoengine import BaseQuerySet
from dataclasses import dataclass
from .. import db
from dataclasses import dataclass
import json

@dataclass
class ProductType(db.Document):
    """ Product Type Model for storing type related details """
    id:int
    name:str
    code:str

    meta = {'collection': 'product_types', 'queryset_class': BaseQuerySet}
    id = db.IntField(primary_key=True)
    name = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255, required=True)
    code = db.StringField(max_length=255, required=True)

    def __init__(self, id, name, description, code,*args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.id = id
        self.name = name
        self.description = description
        self.code=code

def __repr__(self):
    return "<ProductType '{}'>".format(self.username)


def toJson(self):
    return json.dumps(self, default=lambda o: o.__dict__)
