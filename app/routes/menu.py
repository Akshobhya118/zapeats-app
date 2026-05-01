from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models.menu import MenuItem
from app.models.restaurant import Restaurant

menu = Blueprint('menu', __name__)

@menu.route('/restaurants/<int:restaurant_id>/menu')
@login_required
def list_menu(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    menu_items = MenuItem.query.filter_by(restaurant_id=restaurant_id).all()
    return render_template('menu.html', restaurant=restaurant, menu_items=menu_items)

@menu.route('/restaurants/<int:restaurant_id>/menu/add', methods=['GET', 'POST'])
@login_required
def add_menu_item(restaurant_id):
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        category = request.form.get('category')

        new_item = MenuItem(
            name=name,
            description=description,
            price=float(price),
            category=category,
            restaurant_id=restaurant_id
        )
        db.session.add(new_item)
        db.session.commit()
        flash('Menu item added successfully!', 'success')
        return redirect(url_for('menu.list_menu', restaurant_id=restaurant_id))

    return render_template('menu.html')