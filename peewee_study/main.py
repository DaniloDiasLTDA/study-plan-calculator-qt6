
from database import db,Users,Announcement

from peewee import *

db.connect()

db.create_tables([Users, Announcement])

# try:
#     user = Users.create(
#             name="Danilo Dias",
#             email="dias@gmail.com",
#             password="000111"
#         )
# except IntegrityError:
#     print({'error': 'Este usuario já está cadastrado.'})


# try:
#     user = Users.create(
#             name="Luis Souza",
#             email="souzaluis@hotmail.com",
#             password="000111"
#         )
# except IntegrityError:
#     print({'error': 'Este usuario já está cadastrado.'})


# try:
#     user = Users.create(
#             name="Agatha Dantas",
#             email="datas@outlook.com",
#             password="000111"
#         )
# except IntegrityError:
#     print({'error': 'Este usuario já está cadastrado.'})


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


# luiz = Users.get(Users.email == 'souzaluis@hotmail.com')

# announ = Announcement.create(
#     user = luiz,
#     title = "Captação: Shopping estrada do coco",
#     description = "Tirar fotos nas entradas das lojas do terreo.",
#     value = 600.00
# )
# announ = Announcement.create(
#     user = luiz,
#     title = "Video Maker: PizzaHut",
#     description = "Gravar o preparo da pizza.",
#     value = 1200.00
# )
# announ = Announcement.create(
#     user = luiz,
#     title = "Renderizar Videos: GameStation",
#     description = "Renderizar os videos da captação do shopping.",
#     value = 3200.00
# )

# user = Users.get(Users.email == 'dias@gmail.com')

# print(f'ID: {user.id}, Nome: {user.name}, e-mail: {user.email}')

# print("Novo Anúncio: ", announ.id, announ.title)

print('Anuncíos Luiz:')
announ_luiz = Announcement.select().join(Users).where(
    Users.email == "souzaluis@hotmail.com"
)
for announ in announ_luiz:
    print(f'Anun id: {announ.id}, Title Anun: {announ.title},Value: {announ.value}')

Announcement.delete().execute()

print('Anúncios disponíveis: ', Announcement.select().count())

