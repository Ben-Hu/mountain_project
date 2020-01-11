.PHONY: init
init:
	pip install pipenv --upgrade
	pipenv install --dev

.PHONY: format
format:
	pipenv run black .

.PHONY: check_format
check_format:
	pipenv run black . --check --diff

.PHONY: lint
lint: flake8 mypy

.PHONY: flake8
flake8:
	pipenv run flake8 .

.PHONY: mypy
mypy:
	pipenv run mypy .

.PHONY: test
test:
	pipenv run python -m pytest -v tests

.PHONY: coverage
coverage:
	pipenv run pytest \
		--verbose \
		--cov-report term \
		--cov-report html:coverage/html \
		--cov-report xml:coverage/cover.xml \
		--cov-report annotate:coverage/annotate \
		--cov=mountain_project \
		tests