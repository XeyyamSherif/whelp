from celery import Celery

celery_app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='redis://localhost')

@celery_app.task
def my_task(data: dict):
    return data


