###
## addTask.py :Executing a simple task
###

from celery import Celery

app = Celery('addTask',broker='amqp://guest@localhost//')

@app.task
def operasi(x, y):
    print('\n Task Operasi')
    return print(x + y)

@app.task
def harapan(hope):
    print('\n Task Harapan')
    return print(hope)

