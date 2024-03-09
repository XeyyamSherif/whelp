from celery import Celery

celery_app = Celery('tasks', broker='pyamqp://guest@rabbitmq-demo//', backend='redis://redis-demo:6379/0')


@celery_app.task
def my_task(data: dict):
    return data


