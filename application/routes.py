from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Player, Team
from application.forms import AddPlayerName, AddPlayerName, AddTeam

@app.route('/')
def home():
    num_Players = Player.query.count()
    Players = Player.query.all()
    Teams = Team.query.all()

    return render_template('index.html', num = num_Players, Players = Players, Teams = Teams)
    
  

@app.route('/create-player', methods=['GET', 'POST'])
def create():
    message = None
    Teams = Team.query.all()
    form = AddPlayerName()
    form.Team_id.choices.extend([(Team.pk, str(Team)) for Team in Teams])
    if request.method == 'POST':
        if not form.validate_on_submit():
            message = "Player name cannot be blank"
            return render_template('add_player.html', form = form, ptitle = "Add Player", message = message)
        FirstName = form.FirstName.data
        LastName = form.LastName.data
        Position = form.Position.data
        Team_id = int(form.Team_id.data)
        new_player = Player(FirstName = FirstName, LastName = LastName, Position = Position, Team_id = Team_id)
        db.session.add(new_player)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_player.html', form = form, ptitle = "Add Player", message = message)

@app.route('/create-team', methods=['GET', 'POST'])
def create_team():
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
            return render_template('add_team.html', form = form, message = message)
        TeamName = form.TeamName.data
        AddNewTeam= Team(TeamName = TeamName)
        db.session.add(AddNewTeam)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_team.html', form = form, message = message)

@app.route('/update/<int:pk>', methods=['GET', 'POST'])
def update(pk):
    player = Player.query.get(pk)
    teams = Team.query.all()
    form = AddPlayerName()
    form.Team_id.choices.extend([(team.pk, str(team)) for team in teams])
    if request.method == 'POST':
        player.FirstName = form.FirstName.data
        player.LastName = form.LastName.data
        player.Position = form.Position.data
        player.Team_id = int(form.Team_id.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_player.html', form = form, ptitle = "Update Player")

@app.route('/delete/<int:i>')
def delete(i):
    player = Player.query.get(i)
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('home'))