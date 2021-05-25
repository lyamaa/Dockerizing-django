from celery import shared_task


@shared_task
def sample_task():
    print("The sample task just ran.")