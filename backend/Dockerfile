FROM python:buster

RUN apt-get update
RUN apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -U pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 8000

CMD [ "python3", "main.py" ]