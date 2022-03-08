from application import db

class Player(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Position = db.Column(db.String(20))
    Team_id = db.Column(db.Integer, db.ForeignKey('team.pk'))
    def __str__(self):
        return f"{self.LastName} {self.FirstName} {self.Position}" 

class Team(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    TeamName = db.Column(db.String(100))
    team_players = db.relationship('Player', backref='team')
    def __str__(self):
        return f"{self.TeamName}" 