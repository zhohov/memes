FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /backend/memes_service

COPY pyproject.toml poetry.lock /backend/memes_service/
RUN pip install --upgrade pip && pip install poetry
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /backend/memes_service/

EXPOSE 8000

CMD ["poetry", "run", "python", "src/main.py"]