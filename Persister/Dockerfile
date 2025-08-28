FROM python:3.12-slim AS builder

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["sh", "-c", "python -m persister_sub.persister_antisemitic_receives && python -m persister_sub.persister_not_antisemitic_receives"]
