# 1. Use slim Python base image
FROM python:3.13-slim

# 2. Set working directory inside Django app
WORKDIR /app/babyshop_app

# 3. Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements first (for caching)
COPY babyshop_app/requirements.txt /app/requirements.txt

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# 6. Copy the complete project
COPY . /app/

# 7. Expose Django development port
EXPOSE 8000

# 8. Default command (compose will override this)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
