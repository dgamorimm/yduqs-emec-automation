all: install-git install-pyenv install-virtualenv install-libs run

install-git:
	choco install git -y

install-pyenv:
	choco install pyenv-win -y
	$(eval PATH := $(shell where pyenv | awk -F: '{print \$1}')/pyenv-win:$(PATH))
	pyenv install 3.10.11
	pyenv global 3.10.11
	python -V

install-virtualenv:
	python -m venv .venv
	.venv\Scripts\activate

install-libs:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

run:
	python setup.py