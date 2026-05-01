from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models.restaurant import Restaurant

restaurant = Blueprint('restaurant', __name__)

@restaurant.route('/')
@restaurant.route('/restaurants')
@login_required
def list_restaurants():
    restaurants = Restaurant.query.all()
    return render_template('restaurants.html', restaurants=restaurants)

@restaurant.route('/restaurants/<int:id>')
@login_required
def restaurant_detail(id):
    restaurant = Restaurant.query.get_or_404(id)
    return render_template('menu.html', restaurant=restaurant)

@restaurant.route('/restaurants/add', methods=['GET', 'POST'])
@login_required
def add_restaurant():
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        cuisine = request.form.get('cuisine')

        new_restaurant = Restaurant(name=name, location=location, cuisine=cuisine)
        db.session.add(new_restaurant)
        db.session.commit()
        flash('Restaurant added successfully!', 'success')
        return redirect(url_for('restaurant.list_restaurants'))

    return render_template('index.html')