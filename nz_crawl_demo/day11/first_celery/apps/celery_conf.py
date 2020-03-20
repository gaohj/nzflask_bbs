
BROKER_URL = 'redis://127.0.0.1:6379/1'

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'

CELERY_IMPORTS = (
    'apps.task1',
    'apps.task2',
)

