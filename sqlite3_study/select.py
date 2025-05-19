import sqlite3

from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


def find_name():
    try:
        cursor.execute(
            f'SELECT * FROM {TABLE_NAME} '             
        )
        row = cursor.fetchall()
        cursor.close()
        return row
    
    except TypeError:
        print({'error': 'O nome deve ser uma string.'})
    except sqlite3.Error as error:
        print(f"Erro ao acessar o banco de dados: {error}")

row = find_name()
print(row)

cursor.close()
connection.close()