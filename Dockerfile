FROM python:3.6.5-slim

COPY . /src

WORKDIR /src

RUN pip3 install -r requirements.txt

# EXPOSE 8082 # it was added for testing only

CMD ["python", "app.py"]
