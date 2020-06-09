from application import db

class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    holiday = db.Column(db.String(30), nullable=False)
    activity = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'Plan: ', str(self.Plan)
            ])

    def __init__(self, id, holiday, activity):
        self.id = id
        self.holiday = holiday
        self.activity = activity