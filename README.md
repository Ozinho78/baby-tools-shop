# Baby Tools Shop

## Table of Contents
1. [Project Description](#1-project-description)
2. [Quickstart](#2-quickstart)
3. [Local Development Usage](#3-local-development-usage)
4. [Containerized Usage (Docker)](#4-containerized-usage-docker)
5. [Project Structure](#5-project-structure)
6. [Demo Data Script](#6-demo-data-script)
7. [Notes on Code Adjustments](#7-notes-on-code-adjustments)
8. [License](#8-license)

---

## 1. Project Description

**Baby Tools Shop** is a demonstration web application built using **Django**.  
It provides:

- A simple product catalog  
- Category-based product organization  
- Django admin integration  
- Image upload support  
- A clean, educational architecture for learning Django basics  

This repository contains the Django project, a Dockerfile for containerization,  
docker-compose setup, a Quickstart dataset script, and documentation.

Development happens inside the **`feature/containerizing`** branch, while the  
`main` branch remains untouched as the clean fork baseline. All changes are  
reviewed through a Pull Request.

---

## 2. Quickstart

This section explains how to run the project **locally** (without Docker).  

### Prerequisites
Before starting, ensure the following tools are installed:

- **Python 3.12+**
- **Git**
- **Virtual environment (venv)**

---

## 2.1 Clone the Repository

Clone the repository and switch into the project directory:

```bash
git clone https://github.com/Ozinho78/baby-tools-shop.git
cd baby-tools-shop
```

## ⚠️ Switch to the feature branch (contains the latest containerization work)
```bash
git switch feature/containerizing
```

## 2.2 Setup Virtual Environment

The virtual environment must be created inside the babyshop_app folder:
```bash
cd babyshop_app
python -m venv venv
.\venv\Scripts\activate
```

## 2.3 Install Dependencies
```bash
pip install -r requirements.txt
```

## 2.4 Apply Database Migrations
```bash
python manage.py migrate
```

## 2.5 Create Superuser
```bash
python manage.py createsuperuser
```

## 2.6 Loading Demo Data (without images)
```bash
python create_demo_data.py
```

## 2.7 Start Development Server
```bash
python manage.py runserver
```

The app will be available at:
👉 http://127.0.0.1:8000/

---

## ⚠️ Python Compatibility Note (Important)

This project was originally developed with Python < 3.9.
If you use Python 3.12+, some imports in products/models.py must be removed or commented out:
```bash
# from distutils.command.upload import upload
# from email.policy import default
# from enum import unique
# from pyexpat import model
# from unicodedata import name
```

These lines reference deprecated modules that are no longer available in modern Python versions.

---

## 3. Local Development Usage

Once the Quickstart setup is completed, you can continue local development using:

### 3.1 Run the development server
```bash
python manage.py runserver
```

### 3.2 Create or edit models

Models are located inside the products and babyshop apps.
After modifying models, run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3.3 Access Django Admin
```bash
http://127.0.0.1:8000/admin
```
Use the superuser you created during Quickstart.

### 3.4 Uploaded images

Uploaded product images are stored under:
```bash
babyshop_app/media/
```
This folder is automatically created when the first image is uploaded.

---

## 4. Containerized Usage (Docker)

This project includes a full Docker setup consisting of:

- `Dockerfile`  
- `docker-compose.yml`  
- Persistent volumes  
- Automatic migrations  
- Automatic static file collection  

This allows the application to run identically on any system without needing a local Python installation.

---

### 4.1 Requirements
To run the containerized version, install:

- **Docker**
- **Docker Compose**

Verify installation:

```bash
docker --version
docker compose version
```

### 4.2 Build the container image
From the repository root:
```bash
docker compose build
```

### 4.3 Start the application
```bash
docker compose up -d
```

This will automatically:
 - Apply database migrations
 - Collect static files
 - Start Django inside the container
 - Mount persistent volumes for DB, media, and static files
 - Expose the app on port 8025 of your VM

### 4.4 Access the application

The Docker container maps internal port 8000 to external port 8025:
```bash
http://<YOUR-SERVER-IP>:8025
```


Example (local test):
```bash
http://127.0.0.1:8025
```

### 4.5 Stop the container
```bash
docker compose down
```

All data remains preserved thanks to Docker volumes.

### 4.6 View logs
```bash
docker compose logs -f
```

### 4.7 Rebuild after code changes
```bash
docker compose down
docker compose build --no-cache
docker compose up -d
```






