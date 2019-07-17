FROM python:3.6.5-slim

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8082

CMD ["python", "app.py"]
