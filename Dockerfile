FROM python:3.9-slim

WORKDIR /app

COPY config.py .
COPY shared_resources.py .
COPY producer.py .
COPY consumer.py .
COPY main.py .

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]