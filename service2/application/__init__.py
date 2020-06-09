from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from random import random
from os import getenv


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('PROJECT2_DB_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def Country():
   number = random.randint(1, 10)
   country = Country.query.filter_by(id=number).first
   return str(country)


    #country = select.order_by(func.rand(country_db)).limit(10)
    #country = holiday.query.all()
 #   country = random.choice(holiday.query.all())
 
  #  print(country)
   # return country

#test = random.choice(holiday.query.all())
#print(test)