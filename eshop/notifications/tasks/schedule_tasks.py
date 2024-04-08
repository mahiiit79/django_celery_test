from celery_project.celery_config import app
from datetime import timedelta
from celery.schedules import crontab




# app.conf.beat_schedule = {
#     'task_1':{
#         'task': 'notifications.tasks.schedule_tasks.task1',
#         'schedule': crontab(minute='*/1',hour='*',day_of_month='*',day_of_week='*',month_of_year='*'),
#     },
#     'task_2':{
#         'task':'notifications.tasks.schedule_tasks.task2',
#         'schedule': timedelta(seconds=30),
#     }
#
# }

#
# app.conf.beat_schedule = {
#     'task_1':{
#         'task': 'notifications.tasks.schedule_tasks.task1',
#         'schedule': timedelta(seconds=5),
#     },
#     'task_2':{
#         'task':'notifications.tasks.schedule_tasks.task2',
#         'schedule': timedelta(seconds=10),
#     }
#
# }

@app.task(queue='tasks')
def task_1():
    print('running task 1')



@app.task(queue='tasks')
def task_2():
    print('running task 2')