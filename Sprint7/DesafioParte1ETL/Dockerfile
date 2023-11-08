FROM python:3.8

COPY . arquivos/ /app/

WORKDIR /app

RUN pip install pandas boto3

CMD ["python", "app.py"]
