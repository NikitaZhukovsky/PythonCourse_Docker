from celery import Celery

app = Celery(
    'tasks',
    broker='amqp://guest:guest@rabbitmq:5672//',
    backend='redis://redis:6379/0',
    include=['tasks']
)

