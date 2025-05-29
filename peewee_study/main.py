
import logging

from peewee import IntegrityError

from database import db, User, Announcement

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

db.connect()
db.create_tables([User, Announcement])


DEFAULT_USER_EMAIL = 'souzaluis@hotmail.com'

#TODO: Armazenar os dados em um dicionario, chamar a User.create recursivamente 
try:
    user = User.create(
            name="Danilo Dias",
            email="dias@gmail.com",
            password="000111"
        )
    user = User.create(
            name="Luis Souza",
            email=DEFAULT_USER_EMAIL,
            password="000111"
        )
    user = User.create(
            name="Agatha Dantas",
            email="datas@outlook.com",
            password="000111"
        )
    user = User.create(
        name="ProgamadorPython",
        email="devpython@gmail.com",
        password="000111"
    )
except IntegrityError:
    logger.warning('Este e-mail já está cadastrado.')

luiz = User.get(User.email == DEFAULT_USER_EMAIL)

#TODO: Armazenar os dados em um dicionario, chamar a Announcement.create recursivamente 
try:
    Announcement.create(
        user = luiz,
        title = "Captação: Shopping estrada do coco",
        description = "Tirar fotos nas entradas das lojas do terreo.",
        value = 600.00
    )
    Announcement.create(
        user = luiz,
        title = "Video Maker: PizzaHut",
        description = "Gravar o preparo da pizza.",
        value = 1200.00
    )
    Announcement.create(
        user = luiz,
        title = "Renderizar Videos: GameStation",
        description = "Renderizar os videos da captação do shopping.",
        value = 3200.00
    )
except IntegrityError as error:
    logger.warning(f'Estes anúncios já estão cadastrados. {error}')

user = User.get(User.email == DEFAULT_USER_EMAIL)
logger.info(f'ID: {user.id} - Nome: {user.name} - e-mail: {user.email}')

for announcement in user.announcements:
    logger.info("Novo Anúncio: %s - %s.", announcement.id, announcement.title)

#TODO: Pegar os Announcement e dizer qual o seu usuario

# logger.info('Anuncíos Luiz:')
# announ_luiz = Announcement.select().join(User).where(
#     User.email == "example@example.com"
# )
# for announ in announ_luiz:
#     logger.info(f'Anun id: {announ.id}, Title Anun: {announ.title},Value: {announ.value}')

# # Announcement.delete().execute()

# logger.info('Anúncios disponíveis: ', Announcement.select().count())

