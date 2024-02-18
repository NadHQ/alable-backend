FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
CMD ["uvicorn", "src.main:app","--reload",  "--host", "0.0.0.0", "--port", "8000"]