from app.main.model.user import User
from app.main import db
from datetime import date
from flask import request
from flask import jsonify
import json
from bson.objectid import ObjectId

class UserController:
    def __init__(self):
        pass

    def addUser(self, username, password, email):
        user = User(username=username, email=email, password=password)
        user.save()
        response = jsonify(user)
        response.status_code = 201
        return response
