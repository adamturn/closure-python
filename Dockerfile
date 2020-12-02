FROM python:3.7

COPY src /app/src

CMD ["python", "/app/src/main.py"]
