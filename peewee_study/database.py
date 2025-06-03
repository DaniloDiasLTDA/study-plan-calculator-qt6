from utils import DB_FILE
from datetime import datetime


from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, TextField, DateTimeField, DecimalField


db = SqliteDatabase(DB_FILE)

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()


class Announcement(BaseModel):
    user = ForeignKeyField(User, backref='announcements')
    title = CharField(unique=True)
    description = TextField()
    value = DecimalField()
    created_at = DateTimeField(default=datetime.now)
