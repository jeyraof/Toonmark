# -*- coding: utf-8 -*-

from celery.schedules import crontab
from datetime import timedelta

try:
    from settings import CELERY_BROKER as BROKER_URL
except ImportError:
    BROKER_URL = 'amqp://toonmark:toonmark@localhost:5672/toonmark'

CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'Asia/Seoul'

CELERYBEAT_SCHEDULE = {
    'crawls_per_hour': {
        'task': 'tasks.crawls_per_hour',
        # 'schedule': crontab(hour='*', minute=0),
        'schedule': timedelta(seconds=15),
    }
}

# Admin
ADMINS = (('Jaeyoung Lee', 'jaeyoung@monodiary.net'), )

# Mail-server configuration
# CELERY_SEND_TASK_ERROR_EMAILS = True
SERVER_EMAIL = 'no-reply@toonmark.com'
# EMAIL_HOST = 'mail.vandelay.com'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = 'servers'
# EMAIL_HOST_PASSWORD = 's3cr3t'
