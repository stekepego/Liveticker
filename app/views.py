from app import app, db
from flask import render_template, flash, redirect, request
from flask_wtf import FlaskForm
from .models import Result, Team
from .forms import AddResultForm, AddTeamForm
import datetime

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")

@app.route("/results", methods = ["GET", "POST"])
def results():
    result_list = Result.query.order_by("date desc").all()
    form = FlaskForm()

    if form.validate_on_submit():
        for result in result_list:
            db.session.delete(result)
        db.session.commit()
        result_list = Result.query.all()

    return render_template("results.html", results=result_list,form=form)

@app.route("/add_result", methods=["GET", "POST"])
def add_result():
    form = AddResultForm()
    if form.validate_on_submit():
        hometeam = form.hometeam.data
        homescore = form.homescore.data
        guestteam = form.guestteam.data
        guestscore = form.guestscore.data

        if hometeam == guestteam:
            flash("Heim- und Gastteam müssen sich unterscheiden!")
        else:
            home = Team.query.filter_by(name=hometeam).first()
            if home is None:
                home = Team(name=hometeam)
                flash("Team %s noch nicht vorhanden, wurde erstellt." %(hometeam))

            guest = Team.query.filter_by(name=guestteam).first()
            if guest is None:
                guest = Team(name=guestteam)
                flash("Team %s noch nicht vorhanden, wurde erstellt." %(guestteam))

            add_result_to_db(home, guest, homescore, guestscore)
            flash("Ergebnis hinzugefügt (%r %d - %d %r)" %(hometeam,homescore,guestscore,guestteam))

            return redirect("/results")
    show_errors_in_field(form)

    teams = Team.query.all()
    teamnames = []
    for team in teams:
        teamnames.append(team.name)

    return render_template("add_result.html", title="Ergebnis hinzufügen",
                           form=form, teamnames=teamnames)

@app.route("/teams")
def teams():
    teams = Team.query.all()
    return render_template("teams.html", title="Teams",teams=teams)

@app.route("/add_team", methods=["GET", "POST"])
def add_team():
    form = AddTeamForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        url = form.url.data

        if not Team.query.filter_by(name=name).first() is None:
            flash("Team existiert bereits!")
        else:
            team = Team(name=name, description=description, url=url)
            db.session.add(team)
            db.session.commit()
            return redirect("/teams")
    show_errors_in_field(form)
    return render_template("add_team.html", form=form)

def add_result_to_db(home,guest,homescore,guestscore):
    result = Result(home=home, guest=guest,
                    homescore=homescore,guestscore=guestscore, date=datetime.datetime.utcnow())
    db.session.add(result)
    db.session.commit()

def show_errors_in_field(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" %(getattr(form,field).label.text, error))