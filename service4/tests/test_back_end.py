import unittest, pytest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Plan
from os import getenv
import requests

class TestBase(TestCase):
    def create_app(self):
        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLE=False,
                DEBUG=True
                )
        return app
    
    def setUp(self):
        # called before every test
        db.session.commit()
        db.drop_all()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
#     def test_holiday_view(self):
#         response = self.client.post(url_for('holplan'),
#         data=dict(
#             holiday = "China",
#             activity = "Football"
#         ))
#         self.assertIn(b"China", response.data)

    def test_root(self):
        response = self.client.get(url_for('holidayplan'))
        self.assertEqual(response.status_code, 200)
    
    def mocktest(requests_mock):
        requests_mock.get('http://service2:5001/', text='China')
        requests_mock.get('http://service3:5002/', text='Skiiing')
        def test_con_view(self):
            response = self.client.post(
                url_for('holidayplan'),
                data=dict(
                    holiday = "China",
                    activity = "Skiing"
                ),
            )
            self.assertIn(b"China", response.data)
