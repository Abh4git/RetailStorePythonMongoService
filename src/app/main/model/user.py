from flask import Flask
from mongoengine import Document, StringField, IntField, EmbeddedDocument, EmbeddedDocumentField
from flask_mongoengine import BaseQuerySet
from .. import db
from dataclasses import dataclass

@dataclass()
class User(db.Document):
    """ User Model for storing user related details """
    id: int
    email:str
    username:str

    meta = {'collection': 'users', 'queryset_class': BaseQuerySet}

    id = db.IntField(primary_key=True)
    email = db.StringField(max_length=255, required=True)
    username = db.StringField(max_length=255, required=True)
    description = db.StringField(max_length=255, required=True)
    code = db.StringField(max_length=255, required=True)
    public_id = db.StringField(max_length=255, required=True)
    password_hash = db.StringField(max_length=255, required=True)

    @property
    def password(self):
        raise AttributeError('password: write-only field')
    @password.setter
    def password(self, password):
        pwhash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
        self.password_hash = pwhash

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash,password)
def __repr__(self):
    return "<User '{}'>".format(self.username)
