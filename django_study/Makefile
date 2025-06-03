VENV_NAME = .venv
# VENV_INIT = $(VENV_NAME)/Scripts/Activate


setup: 
	@echo "Ambiente virtual pronto.
	python -m venv $(VENV_NAME)
	python -m pip install --upgrade pip
	pip install -r blog/requirements.txt

run:
	python manage.py runserver

