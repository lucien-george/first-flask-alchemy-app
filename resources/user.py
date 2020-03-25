import sqlite3
from flask_restful import Resource, reqparse
from models.user import User

class UserRegister(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('username', type=str, required=True, help="Username cannot be blank")
  parser.add_argument('password', type=str, required=True, help="Password cannot be blank")

  def post(self):
    data = UserRegister.parser.parse_args()
    if User.find_by_username(data['username']):
      return { "error": "user already exists"}, 400

    user = User(**data)
    user.save()
    return user.json(), 201

class Users(Resource):

  def get(self, _id):
    user = User.find_by_id(_id)
    if user:
      return user.json()
    else:
      return { "error": "Not found" }, 404
