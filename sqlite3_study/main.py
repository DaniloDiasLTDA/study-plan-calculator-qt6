import sqlite3
from sqlite3 import IntegrityError
from pathlib import Path


ROOT_FILE = Path(__file__).parent
DB_FOLDER_NAME = 'data'  # Nome da pasta onde o banco de dados será criado
DB_FOLDER = ROOT_FILE / DB_FOLDER_NAME
DB_NAME = 'db_sqlite3'
DB_FILE = DB_FOLDER / DB_NAME
TABLE_NAME = 'customers'

DB_FOLDER.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


#TODO: Estudar sobre SQL injection
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
sql = f"CREATE UNIQUE INDEX IF NOT EXISTS name ON {TABLE_NAME} (name);"
cursor.execute(sql)


connection.commit()

try:
    cursor.execute(
        f'INSERT INTO {TABLE_NAME} ( name, weight) '
        'VALUES '
        '("Danilo Dias", 100.2),'
        '("Marcela Maçã", 55.33),'
        '("Breno Freire", 2362.62),'
        '("Elion Ações", 421.2)'
    )
    connection.commit()
except IntegrityError:
    print('Dados já salvos no DB')




cursor.close()
connection.close()