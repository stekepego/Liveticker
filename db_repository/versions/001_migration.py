from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
play = Table('play', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('description', String),
    Column('down', Integer),
    Column('distance', Integer),
    Column('result_id', Integer),
)

result = Table('result', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('hometeam', String(length=100)),
    Column('guestteam', String(length=100)),
    Column('homescore', Integer),
    Column('guestscore', Integer),
    Column('date', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['play'].create()
    post_meta.tables['result'].columns['date'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['play'].drop()
    post_meta.tables['result'].columns['date'].drop()
