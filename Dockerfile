From python:3.7-slim-buster

RUN pip install kfp==1.6.2 kfp-server-api==1.6.2

WORKDIR /app
COPY . .

CMD ["python", "train.py"]