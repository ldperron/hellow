import os
from celery import Celery


brokerurl = os.environ['BROKER_URL']

app = Celery('hello', broker=brokerurl)

@app.task
def hello():
    return 'hello world'
