from app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    cuisine = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, default=0.0)
    image_url = db.Column(db.String(300), nullable=True)

    menu_items = db.relationship('MenuItem', backref='restaurant', lazy=True)

    def __repr__(self):
        return f'<Restaurant {self.name}>'