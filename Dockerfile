FROM python:3.12.3-bookworm as base
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.7.1 
ENV PATH="$PATH:$POETRY_HOME/bin"
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN poetry install
COPY ./todo_app /code/todo_app
EXPOSE 5000

FROM base as production
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host=0.0.0.0

FROM base as development
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host=0.0.0.0
