from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from random import randint
from os import getenv
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('PROJECT2_DB_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)

from application.models import Country

@app.route('/', methods=['GET', 'POST'])
def location():
   number = randint(1, 10)
   place = Country.query.filter_by(id=number).first()
   return str(place)
   


    #country = select.order_by(func.rand(country_db)).limit(10)
    #country = holiday.query.all()
 #   country = random.choice(holiday.query.all())
 
  #  print(country)
   # return country

#test = random.choice(holiday.query.all())
#print(test)