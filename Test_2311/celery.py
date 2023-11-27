import os
from celery import Celery

"""
Celery configuration
"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Test_2311.settings')
app = Celery('Test_2311')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
