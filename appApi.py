from flask import Flask, request, jsonify, make_response, abort
import json 
import unittest

app = Flask(__name__)

meals = [{
    'id':1,
    'name':'matumbo',
    'price':150 
},
{
  'id':2,
  'name':'Githeri',
  'price':10   
},

{
  'id':3,
  'name':'Chapo',
  'price':15   
},

{
  'id':4,
  'name':'ngwashe',
  'price':50   
}
]

@app.route('/auth/v1/login', methods=['POST'])
def login():
    return make_response(jsonify({
        "status": "ok"
    }), 200)

@app.route('/auth/v1/signup', methods=['POST'])
def signup():
    data = request.get_json(force=True)
    username = data['username']
    email = data['email']
    password = data['password']
    return make_response(jsonify({
        "status": "ok",
        "username": username,
        "email": email,
        "password": password
    }), 201)



@app.route('/v1/meal', methods=['POST'])
def add_meal_options():
    data = request.get_json(force=True)
    id = data["id"]
    name = data["name"]
    price = data["price"]
    return make_response(jsonify({
        "status": "ok",
        "id": id,
        "name": name,
        "price": price
    }),201)

@app.route('/v1/meal/<int:meal_id>', methods=['PUT'])
def update_meal_info(meal_id):
    data = request.get_json(force=True)
    id = data["id"]
    name = data["name"]
    price = data["price"]
    return make_response(jsonify({
        "status": "ok",
        "id": id,
        "name": name,
        "price": price
    }),201)


@app.route('/v1/meal/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):

    for meal in meals:
        if meal_id == meal['id']:
            meals.remove(meal)
            return make_response(jsonify({"Alert": "Meal deleted"}),200)
    return make_response(jsonify({"Alert": "Meal not found"}),404)
   


@app.route('/v1/menu', methods=['GET'])
def get_menu():
    return jsonify({'meals': meals})

 
@app.route('/v1/meals/<int:meal_id>', methods=['GET'])   
def get_meal_options(meal_id):
    data = request.get_json(force=True)
    id = data["id"]
    name = data["name"]
    price = data["price"]
    return make_response(jsonify({
        "status": "ok",
        "id": id,
        "name": name,
        "price": price
        }),201)





if __name__ == '__main__':
    unittest.main()