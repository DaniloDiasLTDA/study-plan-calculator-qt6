import sqlite3

from pathlib import Path

ROOT_FILE = Path(__name__).parent
DB_FOLDER_NAME = 'sqlite3_study'  # Nome da pasta onde o banco de dados será criado
DB_FOLDER = ROOT_FILE / DB_FOLDER_NAME
DB_NAME = 'db_sqlite3'
DB_FILE = DB_FOLDER / DB_NAME
TABLE_NAME = 'customers'

DB_FOLDER.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#Deleta TODOS dados dentro na tabela
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()

#Zera as sequências dos ids
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

#CUIDADO! TODO: Estudar sobre SQL injection
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()


cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES '
    '(NULL, "Danilo Dias", 100.2), (NULL, "Marcela Maçã", 55.33)'
)
connection.commit()


cursor.close()
connection.close()