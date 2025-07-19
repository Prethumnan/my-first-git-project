FROM python:3.10-slim

WORKDIR /app

COPY python_app.py .

RUN pip install flask

CMD ["python", "python_app.py"]
