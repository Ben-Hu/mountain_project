.PHONY: init
init:
	pip install poetry --upgrade --user
	poetry install

.PHONY: format
format:
	poetry run black .

.PHONY: check_format
check_format:
	poetry run black . --check --diff

.PHONY: lint
lint: flake8 mypy

.PHONY: flake8
flake8:
	poetry run flake8 .

.PHONY: mypy
mypy:
	poetry run mypy .

.PHONY: test
test:
	poetry run python -m pytest tests

.PHONY: coverage
coverage:
	poetry run pytest \
		--cov-report term \
		--cov-report html:coverage/html \
		--cov-report xml:coverage/cover.xml \
		--cov-report annotate:coverage/annotate \
		--cov=mountain_project \
		tests

.PHONY: build
build:
	poetry build