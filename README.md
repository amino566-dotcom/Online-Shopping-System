# 🛒 E-Commerce System — Python OOP

A modular e-commerce application built with **Python and Object-Oriented Programming (OOP)**. This project simulates the core operations of an online shopping platform, including product management, customer accounts, shopping carts, order processing, and multiple payment methods.

The main goal of this project is to apply OOP principles to a practical software development scenario while building a foundation for backend development.

---

## 🚀 Features

### 1. Product Management
- Base product class using abstraction.
- Support for different product types:
  - Physical products
  - Digital products
  - Subscription products
- Product price validation.
- Specialized behavior for different product categories.

### 2. User Management
- Base `User` class.
- Customer and Admin classes using inheritance.
- Encapsulation of sensitive attributes.
- Customer information management.
- Customer order history.
- Admin product management.

### 3. Shopping Cart
- Add products to the cart.
- Remove products.
- Update product quantities.
- Calculate subtotal and total.
- Apply percentage discounts.
- Validate product quantities and stock availability.

### 4. Order Management
- Create orders from shopping carts.
- Store order information.
- Track order status:
  - Pending
  - Paid
  - Shipped
  - Cancelled
- Retrieve order information.
- Maintain a snapshot of purchased items and order totals.

### 5. Payment System
- Abstract payment class.
- Multiple payment implementations:
  - PayPal
  - Credit/Debit Card
  - Cash on Delivery
- Shared payment validation.
- Simulated payment processing.

### 6. Checkout System
- Connect customers, carts, orders, and payment methods.
- Create orders during checkout.
- Process payments.
- Update order status after successful payment.
- Update customer order history.

---

## 🧠 OOP Concepts Applied

This project demonstrates the practical use of:

| Concept | Application |
|---|---|
| Encapsulation | Private attributes and properties |
| Inheritance | Customer, Admin, and specialized products |
| Abstraction | Abstract Product and Payment classes |
| Polymorphism | Different product and payment implementations |
| Composition | Checkout coordinates different objects |
| Magic Methods | Applied where useful |
| Exception Handling | Input validation and error management |

---


├── orders/
│   ├── __init__.py
│
