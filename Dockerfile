FROM python:3.7-alpine

# Install system dependencies.
RUN apk add --update \
    # To build psycopg2.
    build-base \
    postgresql-dev

# Install the application and its dependencies.
COPY . /src/
WORKDIR /src

RUN pip install -r requirements.txt
RUN python setup.py install

ENTRYPOINT /bin/sh
