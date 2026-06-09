# Colombo Shoe Fair Booking System

A Python console-based booking system developed as part of an academic programming project. The system simulates an online footwear reservation platform for the Colombo Shoe Fair, allowing customers to reserve footwear items, choose a payment method, update eligible orders, search order details, and calculate total revenue.

## Project Overview

Colombo Shoe Fair is an annual event in Sri Lanka where customers can browse and reserve footwear items before visiting the fair. This application was designed to improve the booking process by allowing users to create orders, receive a unique order number, manage on-site payment orders, and calculate the total revenue generated from all bookings.

## Features

* Display available footwear items with item codes and prices
* Create new customer bookings
* Generate unique order numbers
* Add multiple items and quantities to an order
* Calculate total bill for selected items
* Apply a 3% processing fee for online payments
* Allow on-site payment orders to be modified
* Search orders using the order number
* Display detailed order information
* Calculate total revenue from all bookings
* Store order records using in-memory data structures

## Technologies Used

* Python
* Dictionaries and nested data structures
* Functions and modular programming
* Conditional logic
* Loops and menu-driven programming
* Basic billing and revenue calculation
* Console-based user interaction

## Business Rules Implemented

* Customers can reserve any number of available footwear items
* Each booking receives a unique order number
* Online payments include a 3% processing fee
* On-site payment orders can be updated later
* Online payment orders cannot be modified after booking
* Orders can be searched using the generated order number
* Total revenue can be calculated from all stored bookings

## Available Items

| Item Code | Item                | Unit Price (LKR) |
| --------- | ------------------- | ---------------: |
| S001      | Men’s Leather Shoes |         5,500.00 |
| S002      | Women’s Heels       |         4,000.00 |
| S003      | Casual Sneakers     |         3,200.00 |
| S004      | Children’s Sandals  |         2,000.00 |
| S005      | Running Shoes       |         4,800.00 |
| S006      | Flip-Flops          |         1,200.00 |

## How to Run

1. Download or clone this repository.
2. Open the project folder.
3. Run the Python file:

```bash
python main.py
```

## Learning Outcomes

This project helped strengthen my understanding of Python programming fundamentals, data structures, menu-driven application design, order management logic, payment processing rules, input handling, and basic revenue calculation.

## Future Improvements

* Add file or database storage for saved orders
* Add customer name and contact details
* Improve input validation for quantities and payment options
* Add edit and remove item functionality
* Generate printable invoices or receipts
* Build a graphical user interface
