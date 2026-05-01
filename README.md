# ZapEats - Food Delivery Web Application

A full stack food delivery web application built with Python Flask.

## Tech Stack
- Backend: Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-Bcrypt
- Frontend: HTML, CSS, JavaScript
- Database: SQLite

## Features
- User Registration & Login with authentication
- Browse Restaurants
- View Menu Items
- Add to Cart
- Place Orders
- Order History

## Project Structure
zapeats/
├── app/
│   ├── models/        # Database models
│   ├── routes/        # API routes
│   ├── static/        # CSS & JS files
│   └── templates/     # HTML templates
├── database/          # SQLite database
├── run.py             # App entry point
├── seed.py            # Sample data
└── requirements.txt   # Dependencies

## How to Run
pip install -r requirements.txt
python seed.py
python run.py