from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from flask_login import login_required
from app.models.menu import MenuItem

cart = Blueprint('cart', __name__)

@cart.route('/cart')
@login_required
def view_cart():
    cart_items = session.get('cart', {})
    items = []
    total = 0

    for item_id, quantity in cart_items.items():
        item = MenuItem.query.get(int(item_id))
        if item:
            subtotal = item.price * quantity
            total += subtotal
            items.append({'item': item, 'quantity': quantity, 'subtotal': subtotal})

    return render_template('orders.html', items=items, total=total)

@cart.route('/cart/add/<int:item_id>', methods=['POST'])
@login_required
def add_to_cart(item_id):
    cart_items = session.get('cart', {})
    cart_items[str(item_id)] = cart_items.get(str(item_id), 0) + 1
    session['cart'] = cart_items
    flash('Item added to cart!', 'success')
    return redirect(url_for('cart.view_cart'))

@cart.route('/cart/remove/<int:item_id>', methods=['POST'])
@login_required
def remove_from_cart(item_id):
    cart_items = session.get('cart', {})
    if str(item_id) in cart_items:
        del cart_items[str(item_id)]
        session['cart'] = cart_items
        flash('Item removed from cart!', 'success')
    return redirect(url_for('cart.view_cart'))