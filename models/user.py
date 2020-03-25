import sqlite3
from db import db

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String)
  password = db.Column(db.String)
  restaurants = db.relationship('RestaurantModel', lazy="dynamic")

  def __init__(self, username, password):
    self.username = username
    self.password = password

  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username=username).first()

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def destroy(self):
    db.session.delete(self)
    db.session.commit()

  def json(self):
    return { "id": self.id, "username": self.username, "password": self.password, "restaurants": [restaurant.json() for restaurant in self.restaurants.all()] }
