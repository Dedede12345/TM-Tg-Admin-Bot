# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

WORKDIR /tg-bot

COPY requirements.txt requirements.txt
COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "main/main.py"]