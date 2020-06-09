from application import db

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(30), nullable=False)
    
    
    def __repr__(self):
        return ''.join([
            'activity: ', str(self.activity)
        ]) 
    
    def __init__(self, id, activity):
        self.id = id
        self.activity = activity