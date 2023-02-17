import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj3cel.settings')

app = Celery('proj3cel')

app.config_from_object('django.conf:settings', namespace = 'CELERY_')
app.autodiscover_tasks()

@app.task(bind = True)
def debug_tasks(self):
    print(f'Request: {self.request!r}')