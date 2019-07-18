FROM python:3.6.5-slim

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

# EXPOSE 8082 # it was added for testing only

CMD ["python", "app.py"]
