FROM python:3.11.0-alpine3.16

RUN apk add --no-cache bash
# bcrypt python package dependecies
RUN apk add build-base
RUN apk add --update musl-dev gcc libffi-dev python3-dev

RUN mkdir /app
WORKDIR /app

EXPOSE 8000

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT gunicorn -w 4 -b:8000 --logger-class "gunicorn_logger.CustomLogger" --access-logfile - app:app
