from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Add relationship with Order
    orders = db.relationship('Order', backref='customer', lazy=True)

    def __repr__(self):
        return f"<Customer {self.first_name} {self.last_name}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    # Add relationship with Order
    orders = db.relationship('Order', backref='menu_item', lazy=True)

    def __repr__(self):
        return f"<Menu Item {self.item_name}>"

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Add relationship with Menu
    menu = db.relationship('Menu', backref='restaurant', lazy=True)
    
    def __repr__(self):
        return f"<Restaurant {self.name}>"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"<Order {self.quantity} items>"
