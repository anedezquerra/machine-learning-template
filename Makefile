.PHONY: help install dev setup-dev lint test fmt

help:
	@echo "Targets: install, dev, lint, test, fmt"

install:
	pip install -r requirements.txt

dev:
	pip install -r requirements-dev.txt

setup-dev:
	@echo "Creating virtual environment in .venv and installing dev dependencies"
	python -m venv .venv
	# Use the created venv's python to install packages so activation is not required
	if [ -f .venv/bin/python ]; then \
		.venv/bin/python -m pip install --upgrade pip && \
		.venv/bin/python -m pip install -r requirements-dev.txt; \
	else \
		.venv\Scripts\python -m pip install --upgrade pip && \
		.venv\Scripts\python -m pip install -r requirements-dev.txt; \
	fi

lint:
	black .
	isort .
	flake8

test:
	pytest -q

fmt:
	black .
	isort .
