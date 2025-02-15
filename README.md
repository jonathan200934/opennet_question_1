# Multi-threaded Producer-Consumer Application

This is a Python implementation of the classic Producer-Consumer problem using multithreading. The application demonstrates thread synchronization, queue management, and parallel processing concepts.

## Features

- Multiple producer and consumer threads running concurrently
- Thread-safe queue implementation
- Configurable number of producers and consumers
- Docker support for easy deployment

## Directory Structure
producer_consumer/
├── config.py
├── shared_resources.py
├── producer.py
├── consumer.py
├── main.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md

## Running the Application
docker-compose up
