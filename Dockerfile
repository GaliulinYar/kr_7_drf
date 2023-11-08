FROM python:3

# ENTRYPOINT ["top", "-b"]

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock /code/

RUN apt-get update && apt-get install -y python3 python3-pip curl

# Устанавливаем Poetry в контейнере
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH
# ENV PATH="${PATH}:/root/.local/bin"

# RUN poetry config virtualenvs.create false
# RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install

RUN apt-get update && apt-get install -y redis-server

COPY . /code


# Устанавливаем Celery
RUN pip install celery
RUN pip install djangorestframework-simplejwt
RUN pip install Django
RUN pip install djangorestframework
RUN pip install requests
RUN pip install django-cors-headers
RUN pip install django-celery-beat
