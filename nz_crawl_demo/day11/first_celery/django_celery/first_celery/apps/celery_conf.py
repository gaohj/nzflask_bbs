
BROKER_URL = 'redis://127.0.0.1:6379/1'

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'

CELERY_IMPORTS = (
    'apps.task1',
    'apps.task2',
    'apps.beat_task',
    'apps.sina_spider_task',
)

CELERY_TIMEZONE = 'Asia/Shanghai'

#是否使用本地的时区
CELERY_ENABLE_UTC = False

#重写task的属性
CELERY_ANNOTATIONS = {'apps.task1.add':{'rate_limit':'10/s'}}

#并发worker 数量
CELERY_CONCURRENCY = 6
# 每次 worker 去任务队列中取任务的 数量
CELERY_PREFETH_MULTIPLIRE = 6

#每个worker执行多少次就会被杀掉
CELERY_MAX_TASKS_PRE_CHILD = 5


#单个任务执行的最大时间
CELERY_TASK_TIME_LIMIT = 60*3

#任务结果执行的超时时间
CELERY_TASK_RESULT_EXPIRES = 1000

from kombu import Queue
CELERY_QUEUES = (
    Queue('task1_add',routing_key='task1_add'),
    Queue('task1_add2',routing_key='task1_add2'),
    Queue('task2_add3',routing_key='task2_add3'),
    Queue('beat_task',routing_key='beat_task'),
    Queue('sina_spider_task',routing_key='sina_spider_task'),
)

#给任务分配 queue 和  routing_key
CELERY_ROUTES = {
    'apps.task1.add2':{'queue':'task1_add2','routing_key':'task1_add2'},
    'apps.task2.add3':{'queue':'task2_add3','routing_key':'task2_add3'},
}
from datetime import timedelta
from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    'python1904':{
        'task':'apps.beat_task.beat_task',#要执行的任务的名字
        # 'schedule':timedelta(seconds=5),#要执行的任务的名字
        'schedule':crontab(minute=43,hour=16),#要执行的任务的名字
        'args':(5,8),
        'kwargs':{'name':'kangbazi'},
        'options':{
            'queue':'beat_task',
            'routing_key':'beat_task',
        }
    },
    'spider_task':{
        'task':'apps.sina_spider_task.get_spider',#要执行的任务的名字
        # 'schedule':timedelta(seconds=5),#要执行的任务的名字
        'schedule':crontab(minute=10),#要执行的任务的名字
        'options':{
            'queue':'sina_spider_task',
            'routing_key':'sina_spider_task',
        }
    }
}