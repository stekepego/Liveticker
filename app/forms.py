from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, NumberRange, InputRequired, URL, Optional

class AddResultForm(FlaskForm):
    string_validators = [DataRequired()]
    int_validators = [InputRequired(), NumberRange(min=0)]

    hometeam = StringField("hometeam", validators=string_validators,render_kw={"placeholder":"Heimteam", "id":"hometeam"})
    homescore = IntegerField("homescore", validators=int_validators,render_kw={"placeholder":"Punkte", "id":"hometeam"})
    guestteam = StringField("guestteam", validators=string_validators,render_kw={"placeholder":"Gastteam", "id":"guestteam"})
    guestscore = IntegerField("guestscore", validators=int_validators,render_kw={"placeholder":"Punkte", "id":"guestteam"})

class AddTeamForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()], render_kw={"placeholder": "Teamname", "id":"name"})
    description = StringField("description", render_kw={"placeholder": "Beschreibung", "id":"description"})
    url = StringField("url", validators=[Optional(strip_whitespace=True),URL()], render_kw={"placeholder":"http://www.x-beliebiges-team.de", "id":"url"})