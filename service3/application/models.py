from application import db

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(30), nullable=False)
    
    
    def __repr__(self):
        return str(self.activity)