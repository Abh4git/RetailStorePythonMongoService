from flask import Flask
from mongoengine import Document, StringField, IntField, EmbeddedDocument, EmbeddedDocumentField
from flask_mongoengine import BaseQuerySet
from .. import db

class PaymentType(db.Document):
    """ User Model for storing user related details """
    meta = {'collection': 'payment_methods', 'queryset_class': BaseQuerySet}
    id = db.IntField(primary_key=True)
    name = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255, required=True)
    code = db.IntField()

def __repr__(self):
    return "<ProductType '{}'>".format(self.username)
