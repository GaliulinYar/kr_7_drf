FROM python:3

# ENTRYPOINT ["top", "-b"]

WORKDIR /code

RUN apt-get update && apt-get install -y python3 python3-pip curl

# Устанавливаем Poetry в контейнере
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH
ENV PATH="${PATH}:/root/.local/bin"

# Устанавливаем зависимости с помощью Poetry
COPY pyproject.toml /code
COPY poetry.lock /code

# RUN poetry config virtualenvs.create false
RUN pip install poetry

COPY . /code


# Устанавливаем Celery
RUN pip install celery
RUN pip install rest_framework_simplejwt
RUN pip install Django
RUN pip install djangorestframework
RUN pip install requests