#!/usr/bin/env python3
from flask import request, make_response, session, abort
from flask_restful import Resource
from models import *
from werkzeug.exceptions import Unauthorized
import re

# Local imports
from config import app, db, api

# Add your model imports
from models import *




# Add your model imports

class Signup(Resource):
    def post(self):
        username = request.get_json()["username"]
        email = request.get_json()["email"]
        new_user = User(
            username=username,
            email=email,
        )

        password = request.get_json()["password"]
        new_user.password_hash = password
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id

        # return new_user.to_dict()
        return new_user.to_dict()


api.add_resource(Signup, "/signup")


class Login(Resource):
    def post(self):
        username = request.get_json()["username"]
        user = User.query.filter(User.username == username).first()

        password = request.get_json()["password"]
        if user.authenticate(password):
            session["user_id"] = user.id
            return user.to_dict(rules=("_password_hash",))

        return {"error": "Invalid username or password"}, 401


api.add_resource(Login, "/login")


class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get("user_id")).first()
        if user:
            return user.to_dict(rules=("_password_hash",))
            # return user.to_dict(only=("username",))

        else:
            return {"message": "401: Not Authorized"}, 401


api.add_resource(CheckSession, "/check_session")


class Logout(Resource):
    def delete(self):
        session["user_id"] = None
        return {"message": "204: No Content"}, 204


api.add_resource(Logout, "/logout")


class Tacos(Resource):
    def get(self):
        tacos = Taco.query.all()
        
        # Format the tacos with properly spaced instructions
        formatted_tacos = [
            {
                "taco_id":taco.id,
                "taco_name": taco.taco_name,
                "instructions": taco.instructions.split("\n"),  # Split instructions by newlines
                "time_to_cook": taco.time_to_cook,
                "time_to_prepare": taco.time_to_prepare,
                "image": taco.image,
                
            }
            for taco in tacos
        ]
        
        return make_response(formatted_tacos, 200)

    def post(self):
        data = request.get_json()
        try:
            new_taco = Taco(
                taco_name=data["taco_name"],
                instructions=data["instructions"],
                time_to_cook=data["time_to_cook"],
                time_to_prepare=data["time_to_prepare"],
                image=data.get("image", "images/table-food.jpg")
             
            )
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.add(new_taco)
        db.session.commit()

        return make_response(
            new_taco.to_dict(), 201
        )
    


api.add_resource(Tacos, "/tacos")

class Ingredients(Resource):
    def get(self):
        ingredients = [ingredient.to_dict() for ingredient in Ingredient.query.all()]
        return make_response(ingredients, 200)


api.add_resource(Ingredients, "/ingredients")



class Quantities(Resource):
    def post(self):
        data = request.get_json()
        try:
            new_quant = Quantity(
                quantity=data["quantity"],
                measurement=data["measurement"],
                taco_id=data["taco_id"],
                ingredient_id=data["ingredient_id"],
            )
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.add(new_quant)
        db.session.commit()

        return make_response(new_quant.to_dict(), 201)


api.add_resource(Quantities, "/quantities")


class Users(Resource):
    def get(self):
        users = [
            user.to_dict(
                rules=(
                  
                    "-tacos",
                    "-favorite_tacos",
                )
            )
            for user in User.query.all()
        ]
        return make_response(users, 200)


api.add_resource(Users, "/users")


@app.route('/favorite-taco/<int:taco_id>', methods=['POST'])
def favorite_taco(taco_id):
    if 'user_id' not in session:
        return {"error": "You must be logged in to favorite a taco"}, 401

    user_id = session['user_id']
    favorite = Favorite(user_id=user_id, taco_id=taco_id)
    db.session.add(favorite)
    db.session.commit()

    return {"message": "Taco favorited successfully"}, 200


# class Favorites(Resource):
#     def get(self):
#         # Retrieve the 'username' of the logged-in user from the session or wherever it's stored.
       
#         username = session.get("user_id")  

#         if not username:
#             return {"error": "You must be logged in to view your favorites"}, 401

#         # Query the User model to get the user based on the 'username'
#         user = User.query.filter_by(username=username).first()

#         if user is None:
#             return {"error": "User not found"}, 404

#         # Access the favorite_tacos relationship from the user
#         user_favorites = user.favorite_tacos

#         # Extract the taco information from the favorites
#         favorites = [favorite.to_dict() for favorite in user_favorites]

#         return make_response(favorites, 200)



# api.add_resource(Favorites, "/favorites")

if __name__ == '__main__':
    app.run(port=5555, debug=True)

