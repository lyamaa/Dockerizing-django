FROM python:3.8.5-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN \
  apk add --no-cache curl

# install psycopg2 dependencies
RUN apk update \
  && apk add postgresql-dev gcc python3-dev musl-dev

# pillow dependencies
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

# Install poetry
RUN pip install -U pip \
  && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"
RUN addgroup core && adduser --ingroup core --disabled-password --gecos '' core
WORKDIR /code

RUN mkdir /code/staticfiles
RUN mkdir /code/mediafiles

COPY poetry/pyproject.toml pyproject.toml

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY ./compose/entrypoint .
RUN chmod +x entrypoint

COPY ./compose/start .
RUN chmod +x start

COPY ./compose/start-celery .
RUN chmod +x start-celery

COPY ./compose/start-celery-beat .
RUN chmod +x start-celery-beat

COPY . /code

RUN chown -R core:core /code

USER core

ENTRYPOINT ["/code/entrypoint"]

# run entrypoint.sh
# ENTRYPOINT ["/code/entrypoint.sh"]
