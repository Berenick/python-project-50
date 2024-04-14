lint:
	poetry run flake8 gendiff

install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov