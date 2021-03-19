FROM python:3.6.5-slim

MAINTAINER Salman Waheed "mkdirenv@gmail.com"

WORKDIR /src
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /src

CMD ['flask', 'run' '-h', '0.0.0.0']
