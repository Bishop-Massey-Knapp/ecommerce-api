# E-Commerce API - Project Deliverables

## Database Models

### User Model
- **Fields**: id, name, address, email
- **Relationships**: One-to-many with orders

### Product Model  
- **Fields**: id, product_name, price
- **Relationships**: Many-to-many with orders

### Order Model
- **Fields**: id, order_date, user_id
- **Relationships**: Belongs to user, many-to-many with products
- **Association Table**: order_product (handles many-to-many relationship)

## API Endpoints

### User Endpoints
- `POST /users` - Create new user
- `GET /users` - Get all users  
- `GET /users/<id>` - Get user by ID
- `PUT /users/<id>` - Update user
- `DELETE /users/<id>` - Delete user

### Product Endpoints
- `POST /products` - Create new product
- `GET /products` - Get all products
- `GET /products/<id>` - Get product by ID  
- `PUT /products/<id>` - Update product
- `DELETE /products/<id>` - Delete product

### Order Endpoints
- `POST /orders` - Create new order
- `GET /orders` - Get all orders
- `PUT /orders/<order_id>/add_product/<product_id>` - Add product to order
- `DELETE /orders/<order_id>/remove_product/<product_id>` - Remove product from order
- `GET /orders/user/<user_id>` - Get all orders for user
- `GET /orders/<order_id>/products` - Get all products in order

## Data Serialization

Uses Marshmallow schemas for automatic JSON serialization and validation:
- UserSchema - Handles user data conversion
- ProductSchema - Handles product data conversion  
- OrderSchema - Handles order data with foreign key inclusion

## Key Features

### Database Relationships
- One-to-many: User to Orders
- Many-to-many: Orders to Products (via association table)
- Foreign key constraints for data integrity
- Duplicate prevention on order-product relationships

### Error Handling
- 404 errors for non-existent resources
- 400 errors for validation failures
- Custom error messages for business logic violations

### RESTful Design
- Proper HTTP methods (GET, POST, PUT, DELETE)
- Appropriate status codes (200, 201, 400, 404)
- Consistent JSON request/response format

## Project Structure
```
ecommerce_api/
├── app.py                          # Main Flask application
├── requirements.txt               # Dependencies
├── templates/                     # HTML templates
├── static/                        # Static files (favicon, etc.)
├── E-commerce_API_Collection.postman_collection.json  # API tests
├── TESTING_INSTRUCTIONS.md       # Testing guide
└── PROJECT_DELIVERABLES.md       # This documentation
```

## Testing

### Included Resources
- Complete Postman collection with all endpoints
- Step-by-step testing instructions
- Sample data for database population
- SQL verification queries

### Technologies Used
- Flask 3.1.2
- Flask-SQLAlchemy 3.1.1
- Flask-Marshmallow 1.3.0
- MySQL with mysql-connector-python
- HTML/CSS/JavaScript for web interface

## Setup Instructions

1. Install dependencies: `pip install -r requirements.txt`
2. Configure MySQL database connection in `app.py`
3. Run the application: `python app.py`
4. Access web interface at `http://localhost:6100`
5. Import Postman collection for API testing

The application includes both a RESTful API and a web dashboard for complete e-commerce functionality.
