from application import db

class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    holiday = db.Column(db.String(30), nullable=False)
    activity = db.Column(db.String(30), nullable=False)
