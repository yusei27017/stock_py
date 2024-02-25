FROM python:3.10-slim-bullseye

RUN apt-get update \
  && pip install --no-cache-dir --upgrade pip\
  && pip install pandas requests

WORKDIR /python_dev

ENTRYPOINT ["tail", "-f", "/dev/null"]

# docker build -t stock-dev .