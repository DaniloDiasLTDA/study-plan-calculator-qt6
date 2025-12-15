from pathlib import Path


ROOT_FILE = Path(__file__).parent
DB_FOLDER_NAME = 'data'  # Nome da pasta onde o banco de dados será criado
DB_FOLDER = ROOT_FILE / DB_FOLDER_NAME
DB_NAME = 'freelancers.db'
DB_FILE = DB_FOLDER / DB_NAME


DB_FOLDER.mkdir(parents=True, exist_ok=True)
