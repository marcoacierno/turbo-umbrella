ARG PYTHON_VERSION=3.10.5
ARG NODE_VERSION=16.13.0

FROM python:${PYTHON_VERSION} as python-build

RUN pip install poetry

RUN poetry config virtualenvs.in-project true

RUN mkdir /app/
WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry install

FROM node:${NODE_VERSION} as style-build

RUN mkdir -p /app/theme/static_src
WORKDIR /app/theme/static_src

COPY theme/static_src/package.json theme/static_src/package-lock.json /app/theme/static_src/

RUN npm install

COPY . /app/

RUN npm run build

FROM python:${PYTHON_VERSION} as prod

RUN mkdir /app
WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.in-project true

COPY --from=python-build /app/.venv .venv
COPY --from=style-build /app/theme/static theme/static

COPY . .

RUN SECRET_KEY=abc poetry run python manage.py collectstatic --noinput

EXPOSE 8080

CMD ["poetry", "run", "gunicorn", "--bind", ":8080", "--workers", "2", "superform.wsgi"]
