VENV_NAME = .venv
PYTHON = $(VENV_NAME)/Scripts/python


# VENV_INIT = $(VENV_NAME)/Scripts/Activate


setup: 
	@echo "Ambiente virtual pronto.
	python -m venv $(VENV_NAME)
	python -m pip install --upgrade pip
	pip install -r blog/requirements.txt

run:
	python manage.py runserver
	
# Cria a estrutura do projeto
startapp:
	@echo "Creating Django app: $(APP_NAME)"
	$(PYTHON) manage.py startapp $(APP_NAME)
	@echo "Moving $(APP_NAME) to blog folder..."
	move $(APP_NAME) blog/

# Roda as migrations do projeto
migrate:
	python manage.py migrate
	@echo "Migrate finsh"

# Cria as migrations com base nas models ou alteração delas
migrations:
	python manage.py makemigrations $(app-name)

# Antes de executar as migrations, mostra o slq
sqlmigration:
	python manage.py sqlmigrate polls $(version)

shell:
	python manage.py shell

creatadmin:
	python manage.py createsuperuser

