
from celery_project.celery_config import app
import time


#توی تایم لیمیت کلا تسک متوقف میشه
@app.task(queue='tasks',time_limit=10)
def send_email_to_user():
    time.sleep(6)
    return "(*emeail has been sent to user successfully*)"

#توی تایم اوت توی پس زمینه کارشو انجام میده و فقط خطای تایم اوت نشون میده
def send_email():
    result = send_email_to_user.delay()
    try :
        task_result = result.get(timeout=4)
    except TimeoutError:
        print("task time out")
