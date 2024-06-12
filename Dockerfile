# This Dockerfile specifies the base image as python:3.9-alpine.
# Alpine Linux is a lightweight Linux distribution, and python:3.9-alpine
# is an official Python image that includes Python 3.9 on Alpine Linux.
FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5000

EXPOSE $PORT

VOLUME ["/app/data"]

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT wsgi:app"]
