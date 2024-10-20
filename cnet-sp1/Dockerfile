# service_b/Dockerfile
FROM python:3.9-slim

LABEL service.name="sp1"

WORKDIR /app
COPY . .

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]