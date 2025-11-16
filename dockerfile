# 1. Use slim Python base image
FROM python:3.13-slim

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements first (better caching)
COPY requirements.txt /app/

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy project files AFTER dependencies
COPY . /app/

# 7. Expose Django development port
EXPOSE 8000

# 8. Container entrypoint: Django will be started through docker-compose, not here
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
