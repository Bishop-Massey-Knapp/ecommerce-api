# E-Commerce API

A full-stack e-commerce REST API built with Flask, SQLAlchemy, and MySQL. Features a complete web dashboard, comprehensive CRUD operations, and many-to-many relationships.

## 🌟 Live Demo
- **API**: [Your deployment URL here]
- **Web Dashboard**: [Your deployment URL here]

## 🚀 Features

- **RESTful API** with 15+ endpoints
- **Web Dashboard** with interactive forms
- **Database Models** with proper relationships
- **Many-to-Many** relationships (Orders ↔ Products)
- **Data Validation** using Marshmallow
- **Error Handling** with appropriate HTTP responses
- **CORS Support** for cross-origin requests
- **Sample Data** population scripts

## 🛠️ Tech Stack

- **Backend**: Flask 3.1.2, SQLAlchemy, Marshmallow
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Testing**: Postman Collection included
- **Deployment**: Railway/Render ready

## 📊 Database Schema

### Models
- **User**: id, name, address, email
- **Product**: id, product_name, price  
- **Order**: id, order_date, user_id
- **Order_Product**: Association table for many-to-many relationships

### Relationships
- Users → Orders (One-to-Many)
- Orders ↔ Products (Many-to-Many)

## 🔗 API Endpoints

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

## 🏃‍♂️ Quick Start

### Local Development
```bash
# Clone repository
git clone [your-repo-url]
cd ecommerce_api

# Install dependencies
pip install -r requirements.txt

# Setup MySQL database
mysql -u root -p
CREATE DATABASE ecommerce_api;

# Run application
python app.py
```

### Testing
1. Import `E-commerce_API_Collection.postman_collection.json` into Postman
2. Visit `http://localhost:6100` for web dashboard
3. Follow `TESTING_INSTRUCTIONS.md` for complete testing guide

## 📁 Project Structure
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

## 🌐 Deployment

This application is configured for deployment on:
- Railway (recommended)
- Render
- DigitalOcean App Platform
- Google Cloud Platform

### Environment Variables
- `DATABASE_URL` - MySQL connection string
- `FLASK_ENV` - Set to 'production' for deployment
- `PORT` - Application port (automatically set by most platforms)

## 🧪 Sample Data

The project includes comprehensive sample data:
- 25 realistic users with proper contact information
- 20 diverse products with market pricing
- 25 orders with realistic timestamps
- 51 order-product relationships

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 About

Created as a portfolio project demonstrating full-stack development skills including:
- RESTful API design
- Database modeling and relationships
- Web development (HTML/CSS/JavaScript)
- Testing and documentation
- Production deployment

---

**Contact**: [Your contact information]
# ecommerce-api
