install:
	@poetry install

build:
	@poetry build

lint:
	@poetry run flake8 page_loader

check_right:
	@poetry run page-loader https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8

check_wrong:
	@poetry run page-loader https://ru.wikipedia.o

test:
	@poetry run pytest -vv --cov=page-loader --cov-report xml tests
