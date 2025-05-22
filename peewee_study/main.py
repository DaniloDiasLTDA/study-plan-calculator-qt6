
from database import db,Users,Announcement

from peewee import *

db.connect()

db.create_tables([Users, Announcement])

try:
    user = Users.create(
        name="ProgamadorPython",
        email="devpython@gmail.com",
        password="000111"
    )
except IntegrityError:
    print({'error': 'Este e-mail já está cadastrado.'})

print("Novo usuario:", user.id, user.name, user.email)