from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

# Change Anything Here
@app.task
def add(x, y):
    return x + y
