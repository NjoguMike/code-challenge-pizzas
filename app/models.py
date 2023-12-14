from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    
    serialize_rules = ('-pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    pizzas = db.relationship('Restaurant_Pizza', backref='restaurant')

    def __repr__(self):
        return f'Restaurant(id={self.id}, name={self.name}, address={self.address})'

class Pizzas(db.Model,  SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-restaurant.pizzas',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    restaurant = db.relationship('Restaurant_Pizza' , backref='pizzas')

    def __repr__(self):
        return f'Pizzas(id={self.id}, name={self.name}, ingredients={self.ingredients})'

class Restaurant_Pizza(db.Model,  SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    serialize_rules = ('-pizzas.restaurant','-restaurant.pizzas')

    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # restaurant = db.relationship('Restaurant' , back_populates='restaurant_pizza')
    # pizza = db.relationship('Pizza' , backref='restaurant_pizza')
    
    @validates('price')
    def check_price(self,key,price):
        if 30 < price < 1:
            raise ValueError('Please return a value between 1 and 30')
        return price

    def __repr__(self):
        return f'Restaurant_Pizza(price={self.price})'
# add any models you may need. 