from application import db
from application.models import Country

db.drop_all()
db.create_all()