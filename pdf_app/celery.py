import os
from celery import Celery

from pdf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pdf.settings')

app = Celery('pdf', broker='amqp://guest@localhost//', backend='amqp')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)