from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.restaurant import RestaurantModel

class Restaurant(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('name', type=str)
  parser.add_argument('address', type=str)
  parser.add_argument('user_id', type=int, required=True, help="A user must exist")

  @jwt_required()
  def get(self, _id):
    restaurant = RestaurantModel.find_by_id(_id)
    if restaurant:
      return restaurant.json()
    else:
      return { "error": "Not found" }, 404

  def patch(self, _id):
    restaurant = RestaurantModel.find_by_id(_id)
    data = Restaurant.parser.parse_args()
    if restaurant:
      restaurant.name = data['name']
      restaurant.address = data['address']
      restaurant.save()
      return restaurant.json()
    else:
      return { "error": "not found" }

  def delete(self, _id):
    restaurant = RestaurantModel.find_by_id(_id)
    if restaurant:
      restaurant.destroy()
      return restaurant.json()
    else:
      return { "error": "not found" }, 404


class Restaurants(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('name', type=str)
  parser.add_argument('address', type=str)
  parser.add_argument('user_id', type=int, required=True, help="A user must exist")

  def get(self):
    return [restaurant.json() for restaurant in RestaurantModel.query.all()]

  def post(self):
    data = Restaurants.parser.parse_args()
    restaurant = RestaurantModel(**data)
    restaurant.save()
    return restaurant.json(), 201
