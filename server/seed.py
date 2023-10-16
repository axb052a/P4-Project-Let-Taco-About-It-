#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

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
            Fry Tortillas: Pour 1/2 cup oil in a medium size skillet, heat over medium high heat. Carefully dip a tortilla, if the oil sizzles and bubbles then it is hot enough. Gently lay the tortilla in the oil and fry each side for about 30 seconds, just enough to give some color and add some crispness.
            Shape Tortillas: Remove the tortilla to a paper towel to absorb oil, and carefully fold the tortilla over to create a taco shape.
            Toppings: Fill the tortillas with the ground beef taco meat and add desired toppings''',
        "image": "https://images-ext-1.discordapp.net/external/mTJdym1gB26f0NpE2FAokbfCxgj-hWm11TWQR1BSxgM/https/houseofyumm.com/wp-content/uploads/2021/06/Taco-Meat-9-1024x1536.webp?width=549&height=823",
        "time_to_cook": 20,
        "time_to_prepare": 5,
         
    }
]