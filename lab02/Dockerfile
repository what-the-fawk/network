FROM python:3.12.4-bullseye

RUN apt-get update -y && apt-get install -y iputils-ping

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY main.py /app

CMD ["python", "/app/main.py", "--step", "4", "--ip", "87.240.132.67"]
