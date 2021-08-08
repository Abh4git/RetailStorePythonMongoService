from flask import Flask
from flask_mongoengine import MongoEngine
from mongoengine import Document, StringField, IntField, EmbeddedDocument, EmbeddedDocumentField
from dataclasses import dataclass
from .. import db
from flask_mongoengine import BaseQuerySet

class Customer(db.Document):
    """ User Model for storing user related details """
    meta = {'collection': 'customers',  'queryset_class': BaseQuerySet}

    id = db.IntField(primary_key=True)
    firstname = db.StringField(max_length=255, required=True)
    lastname = db.StringField(max_length=255, required=True)
    profile = db.StringField(max_length=255, required=True)
    email = db.StringField(max_length=255, required=True)
    phone = db.StringField(max_length=255, required=True)
    address_line1 = db.StringField(max_length=255, required=True)
    address_line2 = db.StringField(max_length=255, required=True)
    city =db.StringField(max_length=255, required=True)
    country = db.StringField(max_length=255, required=True)
    paymenttype_id = db.IntField()



def __repr__(self):
    return "<Customer '{}'>".format(self.username)
