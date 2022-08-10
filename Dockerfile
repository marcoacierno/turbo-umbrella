ARG PYTHON_VERSION=3.10.5

FROM python:${PYTHON_VERSION}

RUN pip install poetry
RUN mkdir -p /app

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry install

COPY . .

RUN SECRET_KEY=abc poetry run python manage.py collectstatic --noinput

EXPOSE 8080

CMD ["poetry", "run", "gunicorn", "--bind", ":8080", "--workers", "2", "superform.wsgi"]
