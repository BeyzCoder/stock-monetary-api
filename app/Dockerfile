FROM python:3.12-slim-bookworm

WORKDIR /stock-monetary-api

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /stock-monetary-api/app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]