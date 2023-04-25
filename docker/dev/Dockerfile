FROM python:3.10-buster

COPY . /app

WORKDIR /app

RUN python -m pip install poetry

RUN poetry install

RUN poetry run python -m pip install Pillow

RUN poetry run python -m manage migrate
