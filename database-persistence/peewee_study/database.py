from datetime import datetime

from peewee import (
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKeyField,
    Model,
    SqliteDatabase,
    TextField,
)
from utils import DB_FILE

db = SqliteDatabase(DB_FILE)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()


class Announcement(BaseModel):
    user = ForeignKeyField(User, backref="announcements")
    title = CharField(unique=True)
    description = TextField()
    value = DecimalField()
    created_at = DateTimeField(default=datetime.now)
