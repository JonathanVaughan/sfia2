from flask import Flask, request, render_template
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
@app.route('/home')
def home():
    holplan = Plan.query.all()
    holiData = requests.get('http://service4:5003/').text
    return render_template('home.html', title = 'Holiday', holiday = holiData, holplan = holplan)