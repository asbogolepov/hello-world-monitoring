FROM python:3.8-slim-buster
WORKDIR /app
RUN apt update && apt install curl -y
COPY . .
RUN pip3 install -r requirements.txt
ENV FLASK_APP=flask-hello.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]