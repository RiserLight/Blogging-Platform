# Stage 1: Build dependencies and application
FROM python:3.11-slim AS base

WORKDIR /app

# Copy application code
COPY . .

# Install dependencies in /app/deps but preserve compiled dependencies
RUN pip3 install --no-cache-dir -r requirements.txt psycopg[binary,pool] --target=/app/deps

# Stage 2: Minimal runtime image
FROM gcr.io/distroless/python3-debian12:latest

WORKDIR /app

# Copy application code and dependencies
COPY --from=base /app /app

# Set PYTHONPATH correctly to include site-packages
ENV PYTHONPATH="/app/deps"

# Expose the application port
EXPOSE 8000

# Run the FastAPI application explicitly with Python
CMD ["./blogs/app.py"]
