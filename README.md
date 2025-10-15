# E-Commerce API

A REST API for e-commerce applications built with Flask and MySQL. Includes complete CRUD operations, relationship management, and a web interface for testing and administration.

## Overview

This project implements a full-featured e-commerce backend with user management, product catalog, and order processing capabilities. The API supports many-to-many relationships between orders and products, with proper data validation and error handling.

## Technology Stack

**Backend Framework:** Flask 3.1.2  
**Database:** MySQL with SQLAlchemy ORM  
**Data Serialization:** Marshmallow  
**Frontend:** HTML5, CSS3, JavaScript  
**Testing:** Postman collection included  

## Database Schema

The database consists of three main entities with proper relational constraints:

- **Users**: Customer information (id, name, address, email)
- **Products**: Product catalog (id, product_name, price)  
- **Orders**: Purchase orders (id, order_date, user_id)
- **Order_Product**: Junction table for order-product relationships

**Relationships:**
- Users have many Orders (1:N)
- Orders contain many Products through Order_Product association table (M:N)

## API Endpoints

### Users
- `GET /users` - Get all users
- `GET /users/{id}` - Get user by ID  
- `POST /users` - Create new user
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

### Products
- `GET /products` - Get all products
- `GET /products/{id}` - Get product by ID
- `POST /products` - Create new product
- `PUT /products/{id}` - Update product
- `DELETE /products/{id}` - Delete product

### Orders
- `GET /orders` - Get all orders
- `POST /orders` - Create new order
- `PUT /orders/{order_id}/add_product/{product_id}` - Add product to order
- `DELETE /orders/{order_id}/remove_product/{product_id}` - Remove product from order
- `GET /orders/user/{user_id}` - Get orders by user
- `GET /orders/{order_id}/products` - Get products in order

## Installation and Setup

### Prerequisites
- Python 3.9+
- MySQL 8.0+
- Git

### Local Development
```bash
git clone https://github.com/Bishop-Massey-Knapp/ecommerce-api.git
cd ecommerce-api
pip install -r requirements.txt

# Configure MySQL database
mysql -u root -p -e "CREATE DATABASE ecommerce_api;"

# Start the application
python app.py
```

The application will start at `http://localhost:6100`

### Testing
- Import the Postman collection: `E-commerce_API_Collection.postman_collection.json`
- Access the web dashboard at `http://localhost:6100`
- Refer to `TESTING_INSTRUCTIONS.md` for comprehensive testing procedures

## Project Structure
```
ecommerce_api/
├── app.py                          # Main Flask application
├── requirements.txt               # Dependencies
├── templates/                     # HTML templates
├── static/                        # Static files
├── E-commerce_API_Collection.postman_collection.json
├── TESTING_INSTRUCTIONS.md       # Testing guide
└── PROJECT_DELIVERABLES.md       # Technical documentation
```

## Deployment

The application includes configuration files for multiple deployment platforms:
- Railway (railway.toml)
- Render (Procfile)  
- Google Cloud Platform (app.yaml)

Required environment variables:
- `DATABASE_URL`: MySQL connection string
- `FLASK_ENV`: Set to 'production' for deployment
- `PORT`: Application port (set automatically by hosting platforms)

## Sample Data

The repository includes SQL scripts to populate the database with sample data:
- 25 users with realistic contact information
- 20 products with market-appropriate pricing
- 25 orders with timestamps
- 51 order-product relationship records

## Features

- Complete CRUD operations for all entities
- Many-to-many relationship handling
- Data validation and serialization
- Error handling with appropriate HTTP status codes
- CORS support for cross-origin requests
- Responsive web interface
- Comprehensive API documentation

## License

MIT License

## Contact

Bishop Massey-Knapp  
[GitHub](https://github.com/Bishop-Massey-Knapp)
