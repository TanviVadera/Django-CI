# Django CI/CD with Docker 🚀

A simple Django application containerized using Docker and integrated with GitHub Actions for Continuous Integration (CI).

---

## 🔧 Tech Stack
- Python 3.11
- Django
- Docker
- GitHub Actions

---

## ⚙️ Features
- Dockerized Django application
- Automated testing with GitHub Actions
- Run Django inside a Docker container
- Beginner-friendly DevOps project

---

## ▶️ Run Using Docker

```bash
docker build -t django-image:v3 .
docker run -d -p 8000:8000 --name django-container django-image:v3
