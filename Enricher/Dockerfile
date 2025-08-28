FROM python:3.12-slim AS builder

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["sh", "-c", "python -m enricher_sub.enricher_sub_antisemitic && python -m enricher_sub.enricher_sub_not_antisemitic"]
