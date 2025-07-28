FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY models ./models

# Create folders for PDF input and output results
RUN mkdir -p /app/pdfs /app/outputs

CMD ["python", "app/main.py"]
