# Django CI/CD with Docker 🚀

A simple Django application containerized using Docker and integrated with GitHub Actions.

## Tech Stack
- Python 3.11
- Django
- Docker
- GitHub Actions

## Features
- Dockerized Django application
- Automated testing with GitHub Actions
- Run Django inside a Docker container

## Run Using Docker

1. Build Docker Image:
docker build -t django-image:v3 .

2. Run Docker Container:
docker run -d -p 8000:8000 --name django-container django-image:v3

3. Access in Browser:
http://localhost:8000

## Author
Tanvi Vadera
