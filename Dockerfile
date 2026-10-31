
# 1. Select Python base image
FROM python:3.13-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements file
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application files
COPY app.py .

# 6. Expose application port
EXPOSE 5000

# 7. Start Flask application
CMD ["python", "app.py"]
