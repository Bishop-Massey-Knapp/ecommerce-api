# E-commerce API Testing Instructions

## 1. Database Setup

### MySQL Database Creation:
1. Open MySQL Workbench
2. Connect to your MySQL server
3. Execute this SQL command:
   ```sql
   CREATE DATABASE ecommerce_api;
   ```

## 2. Start the Flask Application

In your terminal (with virtual environment activated):
```bash
cd "/Users/bishop/Desktop/Coding Temple/SQL and API/ecommerce_api"
source venv/bin/activate
python app.py
```

The application will start on `http://127.0.0.1:6100` with debug mode enabled.

## 3. Import Postman Collection

### Import Collection File
1. Open Postman
2. Click "Import" 
3. Select "E-commerce_API_Collection.postman_collection.json"
4. Click "Import"

Alternatively, you can create requests manually using the endpoints listed below.

## 4. API Testing Sequence

### Basic Connection Test
- **GET** `http://localhost:6100/status`
- Expected: JSON response with server status

### Create Test Data
1. **POST Create User**: `http://localhost:6100/users`
   ```json
   {
     "name": "John Doe",
     "address": "123 Main Street, Anytown, USA", 
     "email": "john.doe@email.com"
   }
   ```

2. **POST Create Product**: `http://localhost:6100/products`
   ```json
   {
     "product_name": "iPhone 15 Pro",
     "price": 999.99
   }
   ```

### CRUD Operations Testing
3. **GET All Users**: `http://localhost:6100/users`
4. **GET All Products**: `http://localhost:6100/products`  
5. **GET User by ID**: `http://localhost:6100/users/1`
6. **GET Product by ID**: `http://localhost:6100/products/1`

### Order Operations Testing
7. **POST Create Order**: `http://localhost:6100/orders`
   ```json
   {
     "user_id": 1
   }
   ```

8. **PUT Add Product to Order**: `http://localhost:6100/orders/1/add_product/1`
9. **GET Order Products**: `http://localhost:6100/orders/1/products`
10. **GET User Orders**: `http://localhost:6100/orders/user/1`

### Edge Cases and Validation
11. **PUT Add Same Product Again** (should return duplicate error)
12. **DELETE Remove Product**: `http://localhost:6100/orders/1/remove_product/1`
13. **PUT Update User**: `http://localhost:6100/users/1`
14. **DELETE User**: `http://localhost:6100/users/1`

## 5. Sample Data Population

### Add Users (25 users)
```sql
USE ecommerce_api;

INSERT INTO user (name, email, address) VALUES
('Alice Bennett', 'alice.bennett@example.com', '742 Maple Ave, Portland, OR'),
('Marcus Lee', 'marcus.lee@example.com', '18 Pine Street, Denver, CO'),
('Sophia Carter', 'sophia.carter@example.com', '390 Oak Drive, Austin, TX'),
('Daniel Rivera', 'daniel.rivera@example.com', '55 Cedar Blvd, Miami, FL'),
('Chloe Nguyen', 'chloe.nguyen@example.com', '827 Birch Lane, Seattle, WA'),
('Ryan Brooks', 'ryan.brooks@example.com', '64 Walnut St, Boston, MA'),
('Isabella Torres', 'isabella.torres@example.com', '912 Cherry Court, Phoenix, AZ'),
('James Patel', 'james.patel@example.com', '305 Aspen Rd, Chicago, IL'),
('Ella Morris', 'ella.morris@example.com', '78 Willow Way, Nashville, TN'),
('Logan Murphy', 'logan.murphy@example.com', '123 Sycamore St, Dallas, TX'),
('Harper Kim', 'harper.kim@example.com', '451 Poplar Ave, San Diego, CA'),
('Ethan Wright', 'ethan.wright@example.com', '987 Spruce Dr, Columbus, OH'),
('Lily Adams', 'lily.adams@example.com', '630 Hickory Ln, Madison, WI'),
('Owen Foster', 'owen.foster@example.com', '214 Magnolia St, Atlanta, GA'),
('Ava Ramirez', 'ava.ramirez@example.com', '52 Redwood Blvd, Kansas City, MO'),
('Jack Sullivan', 'jack.sullivan@example.com', '871 Beechwood Ct, Indianapolis, IN'),
('Mia Thompson', 'mia.thompson@example.com', '333 Dogwood Pl, Salt Lake City, UT'),
('Noah Chen', 'noah.chen@example.com', '709 Hemlock Ave, Raleigh, NC'),
('Grace Walker', 'grace.walker@example.com', '95 Linden St, Tampa, FL'),
('Caleb Scott', 'caleb.scott@example.com', '427 Cottonwood Dr, Minneapolis, MN'),
('Aria Hughes', 'aria.hughes@example.com', '188 Palm St, Las Vegas, NV'),
('Benjamin Reed', 'benjamin.reed@example.com', '534 Juniper Rd, Omaha, NE'),
('Zoe Mitchell', 'zoe.mitchell@example.com', '602 Alder Ct, New Orleans, LA'),
('Lucas Perry', 'lucas.perry@example.com', '48 Maplewood Ave, Cincinnati, OH'),
('Natalie Brooks', 'natalie.brooks@example.com', '270 Chestnut Blvd, Richmond, VA');
```

### Add Products (20 products)
```sql
INSERT INTO product (product_name, price) VALUES
('iPhone 15 Pro', 999.99),
('MacBook Pro 14"', 1999.99),
('iPad Air', 599.99),
('AirPods Pro', 249.99),
('Apple Watch Series 9', 399.99),
('Samsung Galaxy S24', 899.99),
('Dell XPS 13 Laptop', 1299.99),
('Sony WH-1000XM5 Headphones', 399.99),
('Nintendo Switch OLED', 349.99),
('Tesla Model S Plaid (Toy)', 89.99),
('Dyson V15 Vacuum', 749.99),
('KitchenAid Stand Mixer', 379.99),
('Instant Pot Duo 7-in-1', 99.99),
('Fitbit Charge 5', 149.99),
('Canon EOS R5 Camera', 3899.99),
('Bose SoundLink Revolve+', 299.99),
('Roomba j7+ Robot Vacuum', 849.99),
('Hydro Flask Water Bottle', 39.99),
('Patagonia Down Jacket', 229.99),
('Allbirds Tree Runners', 98.99);
```

### Add Orders (25 orders)
```sql
INSERT INTO customer_order (user_id, order_date) VALUES
(1, '2025-09-01 10:30:00'),
(2, '2025-09-02 14:15:00'),
(3, '2025-09-03 09:45:00'),
(4, '2025-09-04 16:20:00'),
(5, '2025-09-05 11:10:00'),
(6, '2025-09-06 13:55:00'),
(7, '2025-09-07 08:30:00'),
(8, '2025-09-08 15:40:00'),
(9, '2025-09-09 12:25:00'),
(10, '2025-09-10 17:00:00'),
(11, '2025-09-11 09:15:00'),
(12, '2025-09-12 14:30:00'),
(13, '2025-09-13 10:45:00'),
(14, '2025-09-14 16:10:00'),
(15, '2025-09-15 11:35:00'),
(16, '2025-09-16 13:20:00'),
(17, '2025-09-17 08:50:00'),
(18, '2025-09-18 15:25:00'),
(19, '2025-09-19 12:40:00'),
(20, '2025-09-20 17:15:00'),
(21, '2025-09-21 09:05:00'),
(22, '2025-09-22 14:50:00'),
(23, '2025-09-23 10:20:00'),
(24, '2025-09-24 16:35:00'),
(25, '2025-09-25 11:55:00');
```

### Add Order-Product Relationships (Many-to-Many)  
```sql
INSERT INTO order_product (order_id, product_id) VALUES
(1, 1), (1, 4),
(2, 2),
(3, 3), (3, 5),
(4, 6), (4, 8),
(5, 7), (5, 14),
(6, 9), (6, 18),
(7, 15),
(8, 12), (8, 13),
(9, 11), (9, 17),
(10, 8), (10, 16),
(11, 1), (11, 3), (11, 4), (11, 5),
(12, 14), (12, 18), (12, 20),
(13, 11), (13, 17),
(14, 9), (14, 16),
(15, 15),
(16, 12), (16, 13),
(17, 2), (17, 8),
(18, 6), (18, 4),
(19, 19), (19, 18),
(20, 5), (20, 17),
(21, 8), (21, 16),
(22, 12), (22, 13),
(23, 1), (23, 2), (23, 3),
(24, 14), (24, 20),
(25, 9), (25, 8);
```

## 6. Data Verification

Run these queries to verify the data was inserted correctly:
```sql
-- Check tables were created
SHOW TABLES;

-- Check data counts
SELECT COUNT(*) as user_count FROM user;
SELECT COUNT(*) as product_count FROM product;
SELECT COUNT(*) as order_count FROM customer_order;
SELECT COUNT(*) as order_product_count FROM order_product;

-- Check sample data
SELECT * FROM user LIMIT 5;
SELECT * FROM product LIMIT 5; 
SELECT * FROM customer_order LIMIT 5;
SELECT * FROM order_product LIMIT 10;

-- Check relationships
SELECT u.name, o.id as order_id, o.order_date 
FROM user u 
JOIN customer_order o ON u.id = o.user_id;

SELECT o.id as order_id, p.product_name, p.price
FROM customer_order o
JOIN order_product op ON o.id = op.order_id  
JOIN product p ON op.product_id = p.id;
```

## 7. Expected Results

### Database Tables
- `user` - User information with unique email constraint
- `product` - Product catalog with name and price  
- `customer_order` - Orders linked to users
- `order_product` - Association table for order-product relationships

### API Functionality
- Complete CRUD operations for users and products
- Order management with automatic timestamps
- Many-to-many relationships between orders and products
- Duplicate prevention in order-product associations
- Foreign key constraints maintaining data integrity
- JSON serialization and validation
- Proper error handling with appropriate HTTP status codes

## 8. Troubleshooting

### Common Issues

**Database Connection:**
- Verify MySQL server is running
- Check database credentials in `app.py`
- Ensure `ecommerce_api` database exists

**Dependencies:**
- Install required packages: `pip install -r requirements.txt`
- Activate virtual environment before running Flask

**API Testing:**
- Confirm Flask is running on port 6100
- Include `Content-Type: application/json` in request headers
- Verify JSON request body format matches examples
- Check for typos in endpoint URLs
