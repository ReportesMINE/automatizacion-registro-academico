FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="/app"

#ENTRYPOINT ["python", "-m", "app.main"]
ENTRYPOINT ["bash", "scripts/run.sh"]