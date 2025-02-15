FROM python:3.9-slim

WORKDIR /app

COPY producer_consumer.py .

# Set Python to run unbuffered
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["python", "producer_consumer.py"]