.PHONY: init
init:
	pip install poetry --upgrade --user
	poetry install

.PHONY: format
format:
	poetry run isort --recursive .
	poetry run black .

.PHONY: lint
lint:
	poetry run flake8 .
	poetry run mypy .
	poetry run isort --recursive --check-only .
	poetry run black . --check --diff

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

.PHONY: tox
tox:
	poetry run tox --parallel all