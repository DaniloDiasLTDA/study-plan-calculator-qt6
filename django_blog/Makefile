VENV_NAME = .venv
PYTHON = $(VENV_NAME)/Scripts/python

setup: 
	@echo "Ambiente virtual pronto.
	python -m venv $(VENV_NAME)

init:
	$(PYTHON) -m pip install --upgrade pip
	pip install -r requirements.txt

init-dev: init
	pip install -r requirements-dev.txt

fmt:
	$(PYTHON) -m ruff format .

# Cria a estrutura do projeto
startproject:
	$(PYTHON) -m django startproject app

run: 
	$(PYTHON) manage.py runserver

test:
	coverage run manage.py test
	coverage report

# Criar uma django app
startapp:
	@echo "Creating Django app: $(app-name)"
	$(PYTHON) manage.py startapp $(app-name)

# Roda as migrations do projeto
migrate:
	$(PYTHON) manage.py migrate
	@echo "Migrate finsh"

# Cria as migrations com base nas models ou alteração delas
migrations:
	$(PYTHON) manage.py makemigrations $(app-name)

# Antes de executar as migrations, mostra o slq
sqlmigration:
	$(PYTHON) manage.py sqlmigrate polls $(version)

shell:
	$(PYTHON) manage.py shell

creatadmin:
	$(PYTHON) manage.py createsuperuser

