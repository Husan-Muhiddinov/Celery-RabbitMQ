
from core.celery import app

# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print('Celery is working!')


@app.task(bind=True)
def slow_func(num):
    for i in range(num):
        print(i)