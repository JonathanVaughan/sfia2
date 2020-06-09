from application import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(30), nullable=False)
    
    
    def __repr__(self):
        return ''.join([
            'country: ', str(self.country)
        ]) 
    
    def __init__(self, id, country):
        self.id = id
        self.country = country
    
