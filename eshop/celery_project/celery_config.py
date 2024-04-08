import os
from celery import Celery,Task
from kombu import Exchange, Queue
import logging


class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error('Connection Error occurred in project. Custom task handler handled that')
        else:
            print(f'task id: {task_id} got error')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')
app = Celery('celery_project')
app.Task = CustomTask
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',queue_arguments={'x-max-priority': 10}),
    Queue('dead_letter',routing_key='dead_letter')
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1



app.autodiscover_tasks()


#
# @app.task(queue='tasks')
# def send_message(mobile,message):
#     time.sleep(3)
#     return f'sms send to user with {mobile} number and message was : {message}'
#


# app.conf.task_routes = {
#     'notifications.tasks.send_discount_emails': {'queue': 'queue1'},
#     'notifications.tasks.process_data_for_ml': {'queue': 'queue2'},
# }

# queues => celery,celery:1,celery:2,celery:3

# app.conf.task_default_rate_limit = '1/m'

# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }


