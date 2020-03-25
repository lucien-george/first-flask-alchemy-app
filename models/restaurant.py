import sqlite3
from db import db

class RestaurantModel(db.Model):
  __tablename__ = 'restaurants'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  address = db.Column(db.String)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  user = db.relationship('User')

  def __init__(self, name, address, user_id):
    self.name = name
    self.address = address
    self.user_id = user_id

  def json(self):
    return { "id": self.id, "name": self.name, "address": self.address, "user_id": self.user_id }

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def destroy(self):
    db.session.delete(self)
    db.session.commit()
