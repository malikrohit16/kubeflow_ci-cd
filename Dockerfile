From python:3.7-slim-buster

RUN pip install kfp kfp-server-api

WORKDIR /app
COPY . .

CMD ["python", "train.py"]