from app import db

class DeliveryAgent(db.Model):
    __tablename__ = 'delivery_agents'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    rating = db.Column(db.Float, default=0.0)

    orders = db.relationship('Order', backref='delivery_agent', lazy=True)

    def __repr__(self):
        return f'<DeliveryAgent {self.name}>'