import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister, Users
from resources.restaurant import Restaurants, Restaurant
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'lucien'
api = Api(app)

@app.before_first_request
def create_tables():
  db.create_all()

jwt = JWT(app, authenticate, identity) # creates new endpoint => /auth

api.add_resource(Restaurant, '/restaurant/<_id>')
api.add_resource(Restaurants, '/restaurants')
api.add_resource(UserRegister, '/register')
api.add_resource(Users, '/users/<_id>')

db.init_app(app)

if __name__ == '__main__':
  app.run(port=5000, debug=True)
