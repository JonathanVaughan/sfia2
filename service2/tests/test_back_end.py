import unittest, pytest

from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Country
from os import getenv

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
    def test_location(self):
        response = self.client.get(url_for('location'))
        self.assertEqual(response.status_code, 200)
    
    def test_repr(self):
        cou = Country()
        assert cou == 'Test Country'