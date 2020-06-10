from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from random import randint
from os import getenv



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('PROJECT2_DB_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)

from application.models import Activity

@app.route('/', methods=['GET', 'POST'])
def Activ():
   number = randint(1, 10)
   activity = Activity.query.filter_by(id=number).first()
   return str(activity)
   