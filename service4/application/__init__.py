from flask import Flask, request
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('PROJECT2_DB_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)

from application.models import Plan

@app.route('/', methods=['GET'])
def holidayplan():
    country = requests.get('http://service2:5001/').text
    activity = requests.get('http://service3:5002/').text
    table = Plan(
        country = country,
        activity = activity
    )
    db.session.add(table)
    db.session.commit()
    response = "Country: " + country + "Activity: " + activity 
    return response