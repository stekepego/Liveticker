from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
play = Table('play', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('description', VARCHAR),
    Column('down', INTEGER),
    Column('distance', INTEGER),
    Column('result_id', INTEGER),
)

result = Table('result', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('hometeam', VARCHAR(length=100)),
    Column('guestteam', VARCHAR(length=100)),
    Column('homescore', INTEGER),
    Column('guestscore', INTEGER),
    Column('date', DATETIME),
)

TeamResult = Table('TeamResult', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('resultId', Integer),
    Column('teamId', Integer),
)

plays = Table('plays', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('description', String),
    Column('down', Integer),
    Column('distance', Integer),
    Column('result_id', Integer),
)

results = Table('results', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('hometeam', String(length=100)),
    Column('guestteam', String(length=100)),
    Column('homescore', Integer),
    Column('guestscore', Integer),
    Column('date', DateTime),
)

teams = Table('teams', post_meta,
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
    pre_meta.tables['play'].drop()
    pre_meta.tables['result'].drop()
    post_meta.tables['TeamResult'].create()
    post_meta.tables['plays'].create()
    post_meta.tables['results'].create()
    post_meta.tables['teams'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['play'].create()
    pre_meta.tables['result'].create()
    post_meta.tables['TeamResult'].drop()
    post_meta.tables['plays'].drop()
    post_meta.tables['results'].drop()
    post_meta.tables['teams'].drop()
