FROM python:3.12-slim AS builder

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["sh", "-c", "python -m preprocessor_sub.preprocessor_sub_antisemitic && python -m preprocessor_sub.other_module"]
