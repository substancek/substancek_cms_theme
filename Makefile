# Makefile for substancek_cms_theme
#

# You can set these variables from the command line.
VIRTUALENV_NAME_DEV = python-dev
VIRTUALENV_NAME = python

.PHONY: help install-prerequisites install-dev install-production run-dev run-production python-dev python clean-python-dev clean-python clean-all update-requirements html update-kotti

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  install-prerequisites    to install prerequisites"
	@echo "  install-dev              to build and install a kotti environment suitable for development"
	@echo "  install-production       to build and install a kotti environment suitable for production"
	@echo "  run-dev                  to run substancek_cms_theme in development mode"
	@echo "  run-production           to run substancek_cms_theme in production mode"
	@echo "  python-dev               to make a python-dev virtualenv environment suitable for development"
	@echo "  python                   to make a python virtualenv environment suitable for production"
	@echo "  clean-python-dev         to clean python-dev virtualenv"
	@echo "  clean-python             to clean python virtualenv"
	@echo "  clean-all                to clean all python virtualenvs"
	@echo "  update-requirements      to make requirements.txt"
	@echo "  update-kotti             to update Kotti version. Usage: 'make VERSION=1.1.4 update-kotti'"

install-prerequisites:
	@echo ">>> Install prerequisites"
	sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
	sudo apt-get install build-essential python python-dev python-virtualenv
	@echo ">>> End prerequisites"

install-dev:
	@echo ">>> Install dev"
	make clean-python-dev
	make python-dev
	$(VIRTUALENV_NAME_DEV)/bin/pip install -r devel-requirements.txt
	@echo ">>> End install dev"

install-production:
	@echo ">>> Install production"
	make clean-python
	make python
	make update-requirements
	$(VIRTUALENV_NAME)/bin/pip install -r requirements.txt
	@echo ">>> End install production"

run-dev:
	$(VIRTUALENV_NAME_DEV)/bin/pserve development.ini --reload

run-production:
	$(VIRTUALENV_NAME)/bin/pserve development.ini

python-dev:
	@echo ">>> Create virtualenv dev"
	virtualenv --no-site-packages $(VIRTUALENV_NAME_DEV)
	$(VIRTUALENV_NAME_DEV)/bin/pip install --upgrade pip

python:
	@echo ">>> Create virtualenv production"
	virtualenv --no-site-packages $(VIRTUALENV_NAME)
	$(VIRTUALENV_NAME)/bin/pip install --upgrade pip

clean-python-dev:
	@echo ">>> Clear virtualenv dev"
	rm -rf $(VIRTUALENV_NAME_DEV)

clean-python:
	@echo ">>> Clear virtualenv production"
	rm -rf $(VIRTUALENV_NAME)

clean-all:
	@echo ">>> Clear ALL virtualenvs"
	make clean-python-dev
	make clean-python

update-requirements:
	@echo ">>> Update requirements.txt"
	$(VIRTUALENV_NAME)/bin/pip install -r production-requirements.txt
	$(VIRTUALENV_NAME)/bin/pip freeze -r production-requirements.txt | grep -v substancek_cms_theme | sed '1,2d' > requirements.txt

update-kotti:
	@echo ">>> Updating to version ${VERSION}"
	@echo ">>> Update kotti-requirements.txt"
	wget -O- https://raw.githubusercontent.com/Kotti/Kotti/${VERSION}/requirements.txt | sed '/^Kotti==/d' > kotti-requirements.txt

	@echo ">>> Update devel-requirements.txt"
	sed -e 's/^Kotti\(\[[a-zA-Z,]*\]\)==.*/Kotti\1==${VERSION}/g' devel-requirements.txt > devel-requirements.txt.tmp && mv devel-requirements.txt.tmp devel-requirements.txt
	sed -e 's/^Kotti==.*/Kotti==${VERSION}/g' devel-requirements.txt > devel-requirements.txt.tmp && mv devel-requirements.txt.tmp devel-requirements.txt

	@echo ">>> Update production-requirements.txt"
	sed -e 's/^Kotti\(\[[a-zA-Z,]*\]\)==.*/Kotti\1==${VERSION}/g' production-requirements.txt > production-requirements.txt.tmp && mv production-requirements.txt.tmp production-requirements.txt
	sed -e 's/^Kotti==.*/Kotti==${VERSION}/g' production-requirements.txt > production-requirements.txt.tmp && mv production-requirements.txt.tmp production-requirements.txt

	make update-requirements
