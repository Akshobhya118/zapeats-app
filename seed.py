from app import create_app, db
from app.models.restaurant import Restaurant
from app.models.menu import MenuItem

app = create_app()

with app.app_context():
    r1 = Restaurant(name='Burger Hub', location='Bengaluru', cuisine='Fast Food', rating=4.5)
    r2 = Restaurant(name='Pizza Palace', location='Bengaluru', cuisine='Italian', rating=4.2)
    r3 = Restaurant(name='Biryani House', location='Bengaluru', cuisine='Indian', rating=4.8)
    db.session.add_all([r1, r2, r3])
    db.session.commit()

    m1 = MenuItem(name='Veg Burger', description='Fresh veggie burger', price=120.0, category='Burgers', restaurant_id=1)
    m2 = MenuItem(name='Chicken Burger', description='Spicy chicken burger', price=150.0, category='Burgers', restaurant_id=1)
    m3 = MenuItem(name='Margherita Pizza', description='Classic cheese pizza', price=250.0, category='Pizza', restaurant_id=2)
    m4 = MenuItem(name='Chicken Biryani', description='Hyderabadi dum biryani', price=200.0, category='Biryani', restaurant_id=3)
    db.session.add_all([m1, m2, m3, m4])
    db.session.commit()

    print('Data added successfully!')