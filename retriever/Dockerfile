FROM python:3.12-slim AS builder

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["python","-m", "retriever_manager"]