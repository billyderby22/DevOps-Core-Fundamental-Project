from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from application.models import Player, Team 


class AddPlayerName(FlaskForm):
    FirstName = StringField("Player First Name")
    LastName = StringField("Player Last Name")
    Possition = SelectField("Possition", choices=[('Forward', 'Forward'), ('Midfielder', 'Midfielder'), ('Defender', 'Defender'),('GoalKeeper', 'GoalKeeper')])
    Team_id = SelectField("Players Team", choices=[])
    submit = SubmitField("Add Player")

class AddTeam(FlaskForm):
    TeamName = StringField("Team Name")
    submit = SubmitField("Create Team")
    