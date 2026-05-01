from flask import Blueprint, render_template, session, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models.order import Order
from app.models.menu import MenuItem

order = Blueprint('order', __name__)

@order.route('/orders')
@login_required
def list_orders():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('orders.html', orders=orders)

@order.route('/orders/place', methods=['POST'])
@login_required
def place_order():
    cart_items = session.get('cart', {})

    if not cart_items:
        flash('Your cart is empty!', 'danger')
        return redirect(url_for('cart.view_cart'))

    total = 0
    restaurant_id = None

    for item_id, quantity in cart_items.items():
        item = MenuItem.query.get(int(item_id))
        if item:
            total += item.price * quantity
            restaurant_id = item.restaurant_id

    new_order = Order(
        user_id=current_user.id,
        restaurant_id=restaurant_id,
        total_amount=total,
        status='pending'
    )
    db.session.add(new_order)
    db.session.commit()

    session['cart'] = {}
    flash('Order placed successfully!', 'success')
    return redirect(url_for('order.list_orders'))

@order.route('/orders/<int:order_id>')
@login_required
def order_detail(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('orders.html', order=order)