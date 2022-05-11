from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from random import randint
from time import sleep

app = Flask(__name__)
metrics = PrometheusMetrics(app)

responses_list = [("<p>Hello, World!</p>", 200), ("<p>Internal server error</p>", 502)]

@app.route("/")
def hello_world():
    sleep(randint(0,3))
    return "<p>Hello World!</p>", 200

@app.route("/health")
def health():
    cur = conn.cursor()
    cur.execute("SELECT ACK as status;")
    cur.close()
    return

@app.route("/random")
def random_error():
    sleep(randint(1,3))
    return responses_list[randint(0,1)]

@app.route('/error')
def error():
    return "<p>Internal server error</p>", 502
