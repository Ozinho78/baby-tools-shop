# 1. Base image
FROM python:3.13-slim

# 2. Set project root
WORKDIR /app

# 3. Install deps
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements early for caching
COPY babyshop_app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy full project
COPY . .

# 6. Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
