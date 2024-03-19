FROM python:3.10 

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 

WORKDIR /app 

RUN apt-get update \ 
    && apt-get install -y --no-install-recommends \ 
    postgresql-client \ 
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/ 
RUN pip install --no-cache-dir -r requirements.txt 
COPY . /app/ 

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "library.wsgi:application"]