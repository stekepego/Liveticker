from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
TeamResult = Table('TeamResult', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('resultId', INTEGER),
    Column('teamId', INTEGER),
)

plays = Table('plays', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('description', VARCHAR),
    Column('down', INTEGER),
    Column('distance', INTEGER),
    Column('result_id', INTEGER),
)

results = Table('results', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('hometeam', VARCHAR(length=100)),
    Column('guestteam', VARCHAR(length=100)),
    Column('homescore', INTEGER),
    Column('guestscore', INTEGER),
    Column('date', DATETIME),
)

teams = Table('teams', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=100)),
    Column('description', VARCHAR),
    Column('url', VARCHAR),
)

result = Table('result', post_meta,
    Column('home_id', Integer, primary_key=True, nullable=False),
    Column('guest_id', Integer),
    Column('homescore', Integer),
    Column('guestscore', Integer),
    Column('date', DateTime),
)

team = Table('team', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=100)),
    Column('description', String),
    Column('url', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['TeamResult'].drop()
    pre_meta.tables['plays'].drop()
    pre_meta.tables['results'].drop()
    pre_meta.tables['teams'].drop()
    post_meta.tables['result'].create()
    post_meta.tables['team'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['TeamResult'].create()
    pre_meta.tables['plays'].create()
    pre_meta.tables['results'].create()
    pre_meta.tables['teams'].create()
    post_meta.tables['result'].drop()
    post_meta.tables['team'].drop()
