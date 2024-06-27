.PHONY: lint
lint:
	poetry run flake8 --config .flake8

.PHONY: fmt
fmt:
	poetry run isort src
	poetry run black src
