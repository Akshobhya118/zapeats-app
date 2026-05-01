from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from app.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = 'auth.login'

    from app.routes.auth import auth
    from app.routes.restaurant import restaurant
    from app.routes.menu import menu
    from app.routes.cart import cart
    from app.routes.order import order

    app.register_blueprint(auth)
    app.register_blueprint(restaurant)
    app.register_blueprint(menu)
    app.register_blueprint(cart)
    app.register_blueprint(order)

    return app