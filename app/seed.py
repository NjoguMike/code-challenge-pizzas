from models import Restaurant, Pizzas, Restaurant_Pizza, db
from faker import Faker
import random
from app import app

fake = Faker()

with app.app_context():
    Restaurant.query.delete()
    Restaurant_Pizza.query.delete()
    Pizzas.query.delete()
    db.session.commit()

    restaurants = []

    for rest in range(10):
        restaurant = Restaurant(
            name = f'The {fake.name()}',
            address = fake.address()
        )
        restaurants.append(restaurant)

        db.session.add(restaurant)
        db.session.commit()


    pizza_pick = ['Large','Medium','Small']
    pizzas = []

    for piz in range(10):
        pizza = Pizzas(
            name = f'{random.choice(pizza_pick)} {fake.name()}',
            ingredients = fake.sentence()
        )
        pizzas.append(pizza)

        db.session.add(pizza)
        db.session.commit()

    price_list = [12,23,3,17,23,12,30,19,23,10,21]
    for resto_pizz in range(10):
        # price =1
        rest_piz = Restaurant_Pizza(
            pizza_id = random.choice(pizzas).id,
            restaurant_id = random.choice(restaurants).id,
            price = random.choice(price_list)
        )

        db.session.add(rest_piz)
        db.session.commit()

