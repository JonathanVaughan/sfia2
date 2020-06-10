from application import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(30), nullable=False)
    
    
    def __repr__(self):
        return str(self.country)
        
    

    
