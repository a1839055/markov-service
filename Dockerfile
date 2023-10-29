# syntax=docker/dockerfile:1

FROM python:3.12.0-bookworm
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip3 install -r requirements.txt
CMD ["python", "/app/server.py"]