#!/usr/bin/env python3

# Remote library imports
from flask import Flask, request, make_response, session
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from models import *


# Local imports
from config import app, db, api


@app.route('/')
def index():
    return '<h1>Project Server</h1>'

api = Api(app)

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


class Taco(Resource):
    def get(self):
        tacos = [
            taco.to_dict(rules=("-quantities.ingredient.quantities",))
            for taco in Taco.query.all()
        ]
        for taco in tacos:
            taco["instructions"] = re.split(r"\d+\.\s", taco["instructions"])[1:]
        return make_response(tacos, 200)

    def post(self):
        data = request.get_json()
        try:
            new_taco = Taco(
                taco_name=data["taco_name"],
                instructions=data["instructions"],
                time_to_cook=data["time_to_cook"],
                time_to_prepare=data["time_to_prepare"],
                image="images/table-food.jpg" if not data["image"] else data["image"],
                user_id=session["user_id"],
            )
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.add(new_taco)
        db.session.commit()

        return make_response(
            new_taco.to_dict(rules=("-quantities.ingredient.quantities",)), 201
        )


api.add_resource(Taco, "/Taco")


class Ingredients(Resource):
    def get(self):
        ingredients = [ingredient.to_dict() for ingredient in Ingredients.query.all()]
        return make_response(ingredients, 200)


api.add_resource(Ingredients, "/ingredients")

class Review(Resource):
    def get(self):
        review = [review.to_dict() for review in Review.query.all()]
        return make_response(Review, 200)

    def post(self):
        data = request.get_json()
        try:
            new_review = Review(
                review=data["Review"],
                taco_id=data["taco_id"],
            )
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.add(new_review)
        db.session.commit()

        return make_response(new_review.to_dict(), 201)


api.add_resource(Review, "/review")


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
                    "-collections",
                    "-Taco",
                )
            )
            for user in User.query.all()
        ]
        return make_response(users, 200)


api.add_resource(Users, "/users")


if __name__ == '__main__':
    app.run(port=5555, debug=True)

