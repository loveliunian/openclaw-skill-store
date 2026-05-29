FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/data && python seed_data.py

EXPOSE 5050

CMD ["sh", "-c", "mkdir -p /app/data && python seed_data.py && python app.py"]
