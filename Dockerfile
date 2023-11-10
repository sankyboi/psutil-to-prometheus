# syntax=docker/dockerfile:1
FROM python:3.10
COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python main.py
