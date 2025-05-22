from utils import DB_FILE

from peewee import *


db = SqliteDatabase(DB_FILE)


class Users(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


class Announcement(Model):
    user = ForeignKeyField(Users, backref='users')
    title = CharField()
    description = TextField()
    value = DecimalField()

    class Meta:
        database = db