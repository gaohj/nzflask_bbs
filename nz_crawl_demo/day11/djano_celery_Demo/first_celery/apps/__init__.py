from celery import Celery
app = Celery('kangbazi1904')

app.config_from_object('apps.celery_conf')