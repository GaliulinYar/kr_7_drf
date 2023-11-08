#FROM python:3
#
## ENTRYPOINT ["top", "-b"]
#
#WORKDIR /code
#
#RUN pip install poetry
#
#COPY pyproject.toml poetry.lock /code/
#
#RUN apt-get update && apt-get install -y python3 python3-pip curl
#
## Устанавливаем Poetry в контейнере
#RUN curl -sSL https://install.python-poetry.org | python3 -
#
## Добавляем Poetry в PATH
## ENV PATH="${PATH}:/root/.local/bin"
#
## RUN poetry config virtualenvs.create false
## RUN pip install poetry
#
#RUN poetry config virtualenvs.create false
#RUN poetry install
#
#RUN apt-get update && apt-get install -y redis-server
#
#COPY . /code
#
#
## Устанавливаем Celery
#RUN pip install celery
#RUN pip install djangorestframework-simplejwt
#RUN pip install Django
#RUN pip install djangorestframework
#RUN pip install requests
#RUN pip install django-cors-headers
#RUN pip install django-celery-beat


FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV POETRY_HOME=/bin/poetry
ENV PATH="${POETRY_HOME}/bin/:${PATH}"

EXPOSE 9000

RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y install bash python3 python3-dev postgresql-client  && \
    rm -vrf /var/cache/apk/* && \
    curl -sSL https://install.python-poetry.org  | python - && \
    poetry config virtualenvs.create false --local
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install

RUN pip install redis
RUN pip install celery
RUN pip install django-celery-beat
RUN pip install djangorestframework-simplejwt

RUN pip install drf-yasg
RUN pip install psycopg

COPY . .

# ENTRYPOINT python manage.py migrate & python manage.py runserver