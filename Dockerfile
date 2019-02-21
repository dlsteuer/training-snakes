FROM python:3.6-alpine

RUN apk add build-base

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY main.py boot.sh ./

ENV FLASK_APP main.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]