from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# Database configuration for MySQL
import os

# Use environment variable for production, fallback to local for development
database_url = os.environ.get('DATABASE_URL', 'mysql+mysqlconnector://root:newpassword123@localhost/ecommerce_api')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Association table for Order-Product many-to-many relationship
order_product = db.Table('order_product',
    db.Column('order_id', db.Integer, db.ForeignKey('customer_order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Relationship to orders
    orders = db.relationship('Order', backref='user', lazy=True)

# Order Model
class Order(db.Model):
    __tablename__ = 'customer_order'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Many-to-many relationship with products
    products = db.relationship('Product', secondary=order_product, lazy='subquery',
                             backref=db.backref('orders', lazy=True))

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# MARSHMALLOW SCHEMAS
# User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        
# Order Schema
class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True  
        
# Product Schema  
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

# Initialize schema instances
user_schema = UserSchema()
users_schema = UserSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
    
# Create tables
def create_tables():
    with app.app_context():
        db.create_all()

# CRUD ENDPOINTS

# USER ENDPOINTS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/users', methods=['GET'])
def get_users():
    """GET /users: Retrieve all users"""
    users = User.query.all()
    return users_schema.jsonify(users)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """GET /users/<id>: Retrieve a user by ID"""
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
    """POST /users: Create a new user"""
    try:
        user = user_schema.load(request.json)
        db.session.add(user)
        db.session.commit()
        return user_schema.jsonify(user), 201
    except Exception as e:
        return {"error": str(e)}, 400

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """PUT /users/<id>: Update a user by ID"""
    user = User.query.get_or_404(id)
    try:
        updated_user = user_schema.load(request.json, instance=user, partial=True)
        db.session.commit()
        return user_schema.jsonify(updated_user)
    except Exception as e:
        return {"error": str(e)}, 400

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """DELETE /users/<id>: Delete a user by ID"""
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return {"message": f"User {id} deleted successfully"}, 200

# PRODUCT ENDPOINTS
@app.route('/products', methods=['GET'])
def get_products():
    """GET /products: Retrieve all products"""
    products = Product.query.all()
    return products_schema.jsonify(products)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    """GET /products/<id>: Retrieve a product by ID"""
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product)

@app.route('/products', methods=['POST'])
def create_product():
    """POST /products: Create a new product"""
    try:
        product = product_schema.load(request.json)
        db.session.add(product)
        db.session.commit()
        return product_schema.jsonify(product), 201
    except Exception as e:
        return {"error": str(e)}, 400

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    """PUT /products/<id>: Update a product by ID"""
    product = Product.query.get_or_404(id)
    try:
        updated_product = product_schema.load(request.json, instance=product, partial=True)
        db.session.commit()
        return product_schema.jsonify(updated_product)
    except Exception as e:
        return {"error": str(e)}, 400

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    """DELETE /products/<id>: Delete a product by ID"""
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return {"message": f"Product {id} deleted successfully"}, 200

# ORDER ENDPOINTS
@app.route('/orders', methods=['GET'])
def get_orders():
    """GET /orders: Retrieve all orders"""
    orders = Order.query.all()
    return orders_schema.jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    """POST /orders: Create a new order (requires user ID and order date)"""
    try:
        order = order_schema.load(request.json)
        db.session.add(order)
        db.session.commit()
        return order_schema.jsonify(order), 201
    except Exception as e:
        return {"error": str(e)}, 400

@app.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['PUT'])
def add_product_to_order(order_id, product_id):
    """PUT /orders/<order_id>/add_product/<product_id>: Add a product to an order (prevent duplicates)"""
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    
    # Check if product is already in the order (prevent duplicates)
    if product in order.products:
        return {"error": "Product already exists in this order"}, 400
    
    order.products.append(product)
    db.session.commit()
    return {"message": f"Product {product_id} added to order {order_id}"}, 200

@app.route('/orders/<int:order_id>/remove_product/<int:product_id>', methods=['DELETE'])
def remove_product_from_order(order_id, product_id):
    """DELETE /orders/<order_id>/remove_product/<product_id>: Remove a product from an order"""
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    
    if product not in order.products:
        return {"error": "Product not found in this order"}, 404
    
    order.products.remove(product)
    db.session.commit()
    return {"message": f"Product {product_id} removed from order {order_id}"}, 200

@app.route('/orders/user/<int:user_id>', methods=['GET'])
def get_user_orders(user_id):
    """GET /orders/user/<user_id>: Get all orders for a user"""
    user = User.query.get_or_404(user_id)
    orders = Order.query.filter_by(user_id=user_id).all()
    return orders_schema.jsonify(orders)

@app.route('/orders/<int:order_id>/products', methods=['GET'])
def get_order_products(order_id):
    """GET /orders/<order_id>/products: Get all products for an order"""
    order = Order.query.get_or_404(order_id)
    return products_schema.jsonify(order.products)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/test')
def test_page():
    return render_template('test.html')

@app.route('/api')
def api_info():
    return "Welcome to the E-commerce API!"

@app.route('/status')
def status():
    return {
        "status": "running",
        "message": "Flask server is working!",
        "available_pages": [
            "/ - Main Dashboard (with forms)",
            "/test - Simple test page", 
            "/api - API info",
            "/users - Users API endpoint",
            "/products - Products API endpoint",
            "/orders - Orders API endpoint"
        ]
    }

if __name__ == '__main__':
    create_tables() 
    # Use environment variables for production
    import os
    port = int(os.environ.get('PORT', 6100))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)