from utils import *

import sqlite3

from sqlite3 import IntegrityError


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


#CREATE TABLE TODO: Estudar sobre SQL injection
try:
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'name TEXT,'
        'weight REAL'
        ')'
    )
    connection.commit()
except sqlite3.Error:
    print(f"Não foi possivel criar a tabela.")


#UNIQUE INDEX
try:
    cursor.execute(
        f"CREATE UNIQUE INDEX IF NOT EXISTS name ON {TABLE_NAME} (name);"
        )
    connection.commit()
except sqlite3.Error as e:
    print(f"Arquivo {TABLE_NAME} não encontrado: {e}")


#INSERT
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


#UPDATE
new_name = 'Mario Avila'
person_id = 5
try:
    cursor.execute(f"""
            UPDATE {TABLE_NAME}
            SET name = ?
            WHERE id = ?;
        """, (new_name, person_id))
    connection.commit()
except sqlite3.Error as e:
    print(f"Erro ao atualizar o registro: {e}")


#DELETE
name_delete = 'Breno Freire'
try:
    cursor.execute(f"""
                DELETE FROM {TABLE_NAME}
                WHERE name = ?;
            """, (name_delete,))
    connection.commit()
except sqlite3.Error:
    print(f"Erro ao tentar deletar o usuário.")


cursor.close()
connection.close()