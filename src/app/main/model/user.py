from flask import Flask
from mongoengine import Document, StringField, IntField, EmbeddedDocument, EmbeddedDocumentField, ObjectIdField
from flask_mongoengine import BaseQuerySet
from .. import db, bcryptInst
from dataclasses import dataclass
from bson.objectid import ObjectId


@dataclass()
class User(db.Document):
    """ User Model for storing user related details """
    _id: int
    email: str
    username: str

    meta = {'collection': 'users', 'queryset_class': BaseQuerySet}

    email = db.StringField(max_length=255, required=True, primary_key=True)
    username = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255)
    code = db.StringField(max_length=255)
    public_id = db.StringField(max_length=255, required=True)
    password_hash = db.StringField(max_length=255, required=True)

    def __init__(self, email=None, username=None, password=None, *args, **kwargs):
        super(db.Document, self).__init__(*args, **kwargs)
        self.email = email
        self.username = username
        self.public_id = username
        pwhash = bcryptInst.generate_password_hash(password).decode('utf-8')
        self.password_hash = pwhash

    def check_password(self, password):
        return bcryptInst.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)
