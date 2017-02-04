from app import db

class Team(db.Model):
    __tablename__ = "team"
    __table_args__ = (db.UniqueConstraint("id", "name"),{})
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=True, index=True, unique=True, nullable=False)
    description = db.Column(db.String, unique=True)
    url = db.Column(db.String, unique=True)

    def __init__(self, name, description="", url=""):
        self.name = name
        self.description = description
        self.url = url

    def __repr__(self):
        return "<Team %r" %(self.name)

class Result(db.Model):
    __tablename__ = "result"
    home_id = db.Column(db.Integer, db.ForeignKey("team.id"), primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey("team.id"), primary_key=True)
    homescore = db.Column(db.Integer)
    guestscore = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    # plays = db.relationship("Play", backref="result", lazy="dynamic")

    def __init__(self, home, guest, homescore, guestscore, date):
        self.home = home
        self.guest = guest
        self.homescore = homescore
        self.guestscore = guestscore
        self.date = date
    home = db.relationship(Team, lazy="joined", foreign_keys="Result.home_id", backref="games_ashost")
    guest = db.relationship(Team, lazy="joined", foreign_keys="Result.guest_id", backref="games_asguest")

    def __repr__(self):
        return "<Result %r %d - %d %r>" %(self.hometeam, self.homescore,
                                          self.guestscore, self.guestteam)

# class Play(db.Model):
#     __tablename__ = "play"
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String())
#     down = db.Column(db.Integer)
#     distance = db.Column(db.Integer)
#     result_id = db.Column(db.Integer, db.ForeignKey("result.id"))
#
#     def __repr__(self):
#         return "<Play %r - %d and %d>" %(self.description, self.down, self.distance)
