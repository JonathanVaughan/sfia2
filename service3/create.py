from application import db
from application.models import Activity

db.drop_all()
db.create_all()