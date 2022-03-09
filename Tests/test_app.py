from flask import url_for
from flask_testing import TestCase
from sqlalchemy import true
from application import app, db
from application.models import Player, Team

class TestBase(TestCase):
    def create_app(self): 
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SECRET_KEY = "test secret key",
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )

        return app

    def setUp(self): 
        db.create_all()
        sample_team = Team(TeamName = "Sample Team")
        sample_player = Player(FirstName = "John", LastName = "Smith", Position = "Forward", Team_id = 1)

        db.session.add(sample_team)
        db.session.add(sample_player)
        db.session.commit()
    
    def tearDown(self): 
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Smith', response.data)

class TestAddplayerName(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assert200(response)
        self.assertIn(b'Player First Name', response.data)

    def test_create_post(self):
        response = self.client.post(
            url_for('create'),
            data = dict(FirstName="Bob", LastName='Jones', Position='Defender',Team_id = 1),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Jones', response.data)

class TestAddTeam(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('create_team'))
        self.assert200(response)
        self.assertIn(b'Team Name', response.data)

   