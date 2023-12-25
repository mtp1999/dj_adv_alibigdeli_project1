from celery import shared_task
import time
from django_celery_beat.models import PeriodicTask


@shared_task
def task1():
    time.sleep(3)
    print("Task1 Awake now!!!!!")


@shared_task
def task2():
    print("Task2 Awake now!!!!!")


@shared_task()
def remove_done_tasks():
    tasks = PeriodicTask.objects.all().exclude(name='remove done tasks').exclude(name="celery.backend_cleanup").exclude(last_run_at__isnull=True)
    try:
        tasks.delete()
        # tasks.update(enabled=False)
    except:
        print("Could not delete any task!!!!")
    print("Delete tasks done.")
    print(tasks)
