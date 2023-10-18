#!/usr/bin/env python3
import bcrypt
from models import User
# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import *

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
    
        db.drop_all()
        db.create_all()

        # Seed for Users
        user_list = [
            {"username": "user1", "email": "user1@example.com", "password": "password1"},
            {"username": "user2", "email": "user2@example.com", "password": "password2"},
        ]

        for user_data in user_list:
            user = User(username=user_data["username"], email=user_data["email"])
            # Hash the password using bcrypt
            password_hash = bcrypt.hashpw(user_data["password"].encode("utf-8"), bcrypt.gensalt())
            user._password_hash = password_hash.decode("utf-8")
            db.session.add(user)

        db.session.commit()
        

        taco_list = [
            {
                "taco_name": "Best Ground Beef Taco",
                "taco_type": "Ground Beef",
                "user_id": 1,
                "instructions": '''
                    Cook Ground Beef til no longer pink.
                    Drain any excess grease from the skillet. Then return to the stove and reduce the heat to low.
                    Season: Add the 1/2 cup tomato sauce and taco seasoning. Stir together until the meat is coated in the sauce.
                    Simmer: Allow to simmer for 5 minutes.
                    Fry Tortillas: Pour 1/2 cup oil in a medium-size skillet, heat over medium-high heat. Carefully dip a tortilla, if the oil sizzles and bubbles then it is hot enough. Gently lay the tortilla in the oil and fry each side for about 30 seconds, just enough to give some color and add some crispness.
                    Shape Tortillas: Remove the tortilla to a paper towel to absorb oil, and carefully fold the tortilla over to create a taco shape.
                    Toppings: Fill the tortillas with the ground beef taco meat and add desired toppings''',
                "image": "https://images-ext-1.discordapp.net/external/mTJdym1gB26f0NpE2FAokbfCxgj-hWm11TWQR1BSxgM/https/houseofyumm.com/wp-content/uploads/2021/06/Taco-Meat-9-1024x1536.webp?width=549&height=823",
                "time_to_cook": 20,
                "time_to_prepare": 5,
            },
            {
                "taco_name": "Chicken Taco",
                "taco_type": "Chicken",
                "user_id": 2,
                "instructions": """
                    Preheat the oven to 325°F.
                    In a large pan, heat olive oil over medium heat. Add onions, bell peppers, and garlic.
                    Cook until soft and slightly browned (10-15 minutes).
                    Add chicken, paprika, ancho chili powder, cumin, oregano, cayenne (optional), and salt.
                    Increase heat, stir, and cook until chicken is partially cooked (about 5 minutes).
                    Stir in tomato sauce, then reduce heat to low. Simmer, stirring occasionally, until chicken is fully cooked (12-15 minutes).
                    Sprinkle with cilantro and adjust seasoning.
                    Meanwhile, place taco shells sideways on a baking sheet. Separate the stack, overlapping edges slightly.
                    Bake for 6-7 minutes until crisp.
                    Spoon the chicken into the shells and serve with desired toppings.""",
                "image": "https://i0.wp.com/www.onceuponachef.com/images/2011/02/chicken-tacos-11.jpg?w=1000&ssl=1",
                "time_to_cook": 15,
                "time_to_prepare": 10,
            },
        ]

        for taco_data in taco_list:
            taco = Taco(
                taco_name=taco_data["taco_name"],
                taco_type=taco_data["taco_type"],
                user_id=taco_data["user_id"],
                instructions=taco_data["instructions"],
                image=taco_data["image"],
                time_to_cook=taco_data["time_to_cook"],
                time_to_prepare=taco_data["time_to_prepare"]
            )
            db.session.add(taco)


        db.session.commit()

        # Seed for Ingredients
        ingredient_list = [
             "Beef",
             "Chicken",
             "Tortillas",
             "Cheese",
             "Lettuce",
        ]

        for ingredient_name in ingredient_list:
            ingredient = Ingredient(name=ingredient_name)
            db.session.add(ingredient)

        db.session.commit()

        # Seed for Quantities
        quantity_list = [
            {"quantity": 1, "measurement": "lb", "taco_id": 1, "ingredient_id": 1},
            {"quantity": 2, "measurement": "C", "taco_id": 1, "ingredient_id": 3},
            {"quantity": 1, "measurement": "lb", "taco_id": 2, "ingredient_id": 2},
            {"quantity": 1, "measurement": "C", "taco_id": 2, "ingredient_id": 4},
        ]

        for quantity_data in quantity_list:
            quantity = Quantity(
                quantity=quantity_data["quantity"],
                measurement=quantity_data["measurement"],
                taco_id=quantity_data["taco_id"],
                ingredient_id=quantity_data["ingredient_id"]
            )
            db.session.add(quantity)
    
        db.session.commit()