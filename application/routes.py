from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Player, Team
from application.forms import AddPlayerName, AddPlayerName, AddTeam

@app.route('/')
def home():
    num_Players = Player.query.count()
    Players = Player.query.all()
    return render_template('index.html', num = num_Players, Players = Players)

@app.route('/create-player', methods=['GET', 'POST'])
def create():
    message = None
    Teams = Team.query.all()
    form = AddPlayerName()
    form.Team_id.choices.extend([(Team.pk, str(Team)) for Team in Teams])
    if request.method == 'POST':
        if not form.validate_on_submit():
            message = "Player name cannot be blank"
            return render_template('Add_Player.html', form = form, ptitle = "Add Player", message = message)
        FirstName = form.FirstName.data
        LastName = form.LastName.data
        Possition = form.Possition.data
        Team_id = int(form.Team_id.data)
        new_player = Player(FirstName = FirstName, LastName = LastName, Possition = Possition, Team_id = Team_id)
        db.session.add(new_player)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_player.html', form = form, ptitle = "Add Player", message = message)

@app.route('/create-team', methods=['GET', 'POST'])
def create_project():
    message = None
    form = AddTeam()
    if request.method == 'POST':
        if not form.validate_on_submit():
            message = ""
            for field in ['TeamName']:
                try:
                    err = eval(f"form.{field}.errors[-1]")
                except IndexError:
                    err = ""
                message += err + ", "
            return render_template('Add_Team.html', form = form, message = message)
        TeamName = form.TeamName.Data
        AddTeam= Team(TeamName = TeamName)
        db.session.add(AddTeam)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('AddTeam.html', form = form, message = message)

@app.route('/update/<int:pk>', methods=['GET', 'POST'])
def update(pk):
    Player = Player.query.get(pk)
    Team = Team.query.all()
    form = AddPlayerName()
    form.Team_id.choices.extend([(Team.pk, str(Team)) for Team in Teams])
    if request.method == 'POST':
        Player.FirstName = form.FirstName.data
        Player.LastName = form.LastName.data
        Player.Possition = form.Possition.data
        Player.Team_id = int(form.team_id.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('Add_Player.html', form = form, ptitle = "Update Player")

@app.route('/delete/<int:i>')
def delete(i):
    Player = Player.query.get(i)
    db.session.delete(Player)
    db.session.commit()
    return redirect(url_for('home'))