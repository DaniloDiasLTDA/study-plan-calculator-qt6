
from database import db,Users,Announcement

from peewee import *

db.connect()

db.create_tables([Users, Announcement])

# user = Users.create(
#         name="Danilo Dias",
#         email="dias@gmail.com",
#         password="000111"
#     )
# user = Users.create(
#         name="Luis Souza",
#         email="souzaluis@hotmail.com",
#         password="000111"
#     )
# user = Users.create(
#         name="Agatha Dantas",
#         email="datas@outlook.com",
#         password="000111"
#     )


# try:
#     user = Users.create(
#         name="ProgamadorPython",
#         email="devpython@gmail.com",
#         password="000111"
#     )
# except IntegrityError:
#     print({'error': 'Este e-mail já está cadastrado.'})


# try:
#     user = Users.get(Users.name == "ProgamadorPython")
        
#     if user:
#         user.delete_instance()
# except DoesNotExist:
#     print('Usuario não existe.')

luiz = Users.get(Users.email == 'souzaluis@hotmail.com')

announ = Announcement.create(
    user = luiz,
    title = "Captação: Shopping estrada do coco",
    description = "Tirar fotos nas entradas das lojas do terreo.",
    value = 600.00
)

print("Novo Anúncio: ", announ.id, announ.title)