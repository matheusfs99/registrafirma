FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /registrafirma

COPY requirements.txt /registrafirma/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /registrafirma/

RUN python manage.py migrate

EXPOSE 8000
