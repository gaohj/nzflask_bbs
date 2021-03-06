# Celery   

* 什么是celery

  	1. 灵活、可靠，处理大量消息的分布式系统 （多个节点系统完成某个任务）
   	2. 实时处理的任务队列，支持任务的调度  一个机制  线程 机器之间分发任务的一种机制  
   	3. 开源  、社区活跃
   	4. 纯Python写的   

  

* 使用场景 

  1. 比较耗时的任务 不用等到 程序处理完了以后才知道结果，比如视频转码 ,邮件的发送 消息推送  
  2. 定时任务  定时推送消息  定时爬取数据 定时统计数据   

* 执行的过程   

  celery的一个执行单元 称之为  task(任务)

  1. application (task producer) 任务生产者  
  2. 任务队列 broker （task queue ） redis 或者 rabbitMQ  做消息中间件 
  3. 任务调度  celery beat （task scheduler） 对任务队列中的任务进行调度  
  4. 消费者  worker （task consumer）可以有多个 真正干活的是它 
  5. 处理结果的存储  backend 数据库  缓存 都可以   mysql  redis  rabbitMQ 

  

  ## Pycharm配置环境   

  * 同步 使用服务器虚拟环境

  

  ## 安装   

  ```
  pip install celery[redis]
  ```

  ```
  redis: 
  
  1. wget -c  软件包  
  2.解压 mv 软件包  /usr/local/redis    
  3.cd /usr/local/redis 
  4. make install  
  5./usr/local/redis/src/redis-server  /usr/local/redis/redis.conf 
  
  apt-get install redis-server 
  
  ps -ef | grep redis  
  
  /etc/init.d/redis-server status 
  ```

  ## 实例 

  ```
  from celery  import Celery  
  
  app = Celery(任务名字,broker,backend) 
  ```

  

  ## 启动  broker  

  ```python
celery worker -A celery_app名称 -l INFO
  celery worker -A task -l INFO
  
  -A 包含 app=Celery()文件名  不需要.py  
  -l 显示  日志级别  INFO ERROR等   
  
  
  
  
  
  task.py  
  
  
  from celery import Celery
  
  #broker任务队列  生产者生产任务 放到这里边   消费者从这里边拿
  #backend 存储  消费者处理好以后 将结果存放到这里边
  app = Celery('celery_1904',broker='redis://127.0.0.1:6379/1',backend='redis://127.0.0.1:6379/2')
  
  @app.task
  def hello(name):
      print("hello world:{}".format(name))
      return "hello world:{}".format(name)
  
  @app.task
  def sums(x,y):
      print(x+y)
      return x+y
  
  
  hello.py 
  
  #导入任务
  from task import hello,sums
  
  if __name__ == "__main__":
      hello.delay('world')
      sums.delay(5,10)
  
  ```
  
  
  
  ## 抽取信息到配置文件  
  
  ```python
  apps 
  	__init__.py 
  	celery_conf.py
  	task1.py
  	task2.py 
  	
  hello.py 
  
  
  __init__.py 
  	from celery import Celery
  	app = Celery('kangbazi1904')
  
  	app.config_from_object('apps.celery_conf')
  	
  celery_conf.py
  	BROKER_URL = 'redis://127.0.0.1:6379/1'
  
  	CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
  
  	CELERY_IMPORTS = (
      	'apps.task1',
      	'apps.task2',
  	)
  	
  hello.py 
  	from apps.task1 import add,add2
  	from apps.task2 import add3
  
  	if __name__ == "__main__":
     		# hello.delay('world')
      	# sums.delay(5,10)
      	add.delay(10,20)
     		add2.delay(30,40)
      	add3.delay(50,15)
  
  
  celery -A worker apps
  运行 hello.py  将任务放到任务队列中 等待消费者去处理 并且将结果存到redis 中
  ```
  
  
  
  
  
  ### 常用的配置 信息  
  
  ```python
  
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
  ```
  
  ## 调用 异步任务  
  
  * 任务.delay() 接收的方法简单   
  * 任务.apply_async(args[参数1，参数2],kwargs={key:value}) 可以接受复杂参数    常用  
  * 任务.send_task('task1.add',args=[66,88]) 不经常用  
  
  
  
  ### 启动多个worker 
  
  ```
  celery worker -A celeryapp名 -l INFO -n 名称@%h  
  
  
  -A 包含 app=Celery()文件名  不需要.py  
  -l 显示  日志级别  INFO ERROR等   
  
  -n worker名称    
  
  %h 主机名 包括域名 
  %n 仅限主机名 
  %d 仅限域名   
  
  举例: celery worker -A apps -l INFO -n kangbazi1@%h 
  
  当三个任务 三个worker  那么平均分配   
  当三个任务  两个worker 先一个worker一个任务  谁先完成 另外一个交给哪个worker去处理
  
  
  ```
  
  
  
  ## 配置多个队列    
  
  * apply_async(queue=队列名)
  * app.task(queue=队列名)
  * 配置文件的方式   
  
  ```python
  from kombu import Queue
  CELERY_QUEUES = (
      Queue('task1_add',routing_key='task1_add'),
      Queue('task1_add2',routing_key='task1_add2'),
      Queue('task2_add3',routing_key='task2_add3'),
  )
  
  #给任务分配 queue 和  routing_key
  CELERY_ROUTES = {
      'apps.task1.add2':{'queue':'task1_add2','routing_key':'task1_add2'},
      'apps.task2.add3':{'queue':'task2_add3','routing_key':'task2_add3'},
  }
  ```
  
  
  
  
  
  ## 定时任务 
  
   ### 定时任务参数  
  
  ```
  crontab参数：
  
  crontab()实例化的时候没设置任何参数，都是使用默认值,表示1分钟。crontab常用有5个参数：
  
  minute：分钟，范围0-59；
  
  hour：小时，范围0-23；
  
  day_of_week：星期几，范围0-6。以星期天为开始，即0为星期天。这个星期几还可以使用英文缩写表示，例如“sun”表示星期天；
  
  day_of_month：每月第几号，范围1-31；
  
  month_of_year：月份，范围1-12。
  
  注意：
  
  默认值都是"*"星号，代表任意时刻
  
  举例：
  
  crontab() 每分钟执行
  
  crontab(minute=15) 每小时的15分时刻执行一次任务
  
  crontab(minute=0, hour=0) 每天0点0分时刻执行任务
  
  crontab(minute='59',hour='11') 每天的11点59分执行一次任务
  
  crontab(minute='0,30')
  
  0分和30分执行一次任务，逗号是表示多个表达式or逻辑关系
  
  crontab(hour='9-12,20')
  
  指定9点到12点和20点中每分钟执行任务
  
  其他举例：
  
  crontab(minute=0, hour=0) 每天午夜执行
  
  crontab(minute=0, hour=’*/3’) 每三个小时执行: 午夜, 3am, 6am, 9am, 正午, 3pm, 6pm, 9pm.
  
  crontab(minute=0,hour=’0,3,6,9,12,15,18,21’) 同上
  
  crontab(minute=’*/15’) 每15分钟执行
  
  crontab(day_of_week=’sunday’) 星期日每分钟
  
  crontab(minute=’‘,hour=’‘, day_of_week=’sun’) 同上
  
  crontab(minute=’*/10’,hour=’3,17,22’, day_of_week=’thu,fri’) 每10分钟执行，仅限于周六日3-4 am, 5-6 pm, and 10-11 pm
  
  crontab(minute=0, hour=’/2,/3’) 偶数小时或者能被3整除的小时数执行
  
  crontab(minute=0, hour=’*/5’) 被5整除的小时数，如3pm
  
  crontab(minute=0, hour=’*/3,8-17’) 8am-5pm能被3整除的
  
  crontab(0, 0, day_of_month=’2’) 每月第2天
  
  crontab(0, 0,day_of_month=’2-30/3’) 每偶数天
  
  crontab(0, 0,day_of_month=’1-7,15-21’) 每月1和3周
  
  crontab(0, 0, day_of_month=’11’,month_of_year=’5’) 每年5月11日
  
  crontab(0, 0,month_of_year=’*/3’) 每个季度第1月
  ```
  
  
  
  ```
  linux  定时任务  
  crontab -e 创建定时任务  
  crontab -l 列出所有的定时任务 
  crontab -r 清空所有的计划任务  
  
  
  分      时       日      月     周      命令  
  0-59   0-23    1-31     1-12   0-6  
  
  *       *        *      *      *   
  
  0       */1      *      *      *   每小时执行一次  
  0-5     8,12,15  *      *      *   
  
  
  celery 创建定时任务  跟创建异步任务一样   
  from apps import app
  import time
  def beat_task(x,y,name):
      time.sleep(5)
      print(x+y)
      print(name)
      return 'hello celery beat'
  
  配置文件: 
  
  CELERY_IMPORTS = (
       ...
      'apps.beat_task',
  )
  
  from datetime import timedelta
  from celery.schedules import crontab
  CELERYBEAT_SCHEDULE = {
      'python1904':{
          'task':'apps.beat_task.beat_task',#要执行的任务的名字
          #'schedule':timedelta(seconds=5),#5秒执行一次
          'schedule':crontab(minute=43,hour=16), #详细的小时 分钟 
          'schedule':crontab(hours='*/3'), #每3个小时执行一次
          'args':(5,8),
          'kwargs':{'name':'kangbazi'},
          'options':{
              'queue':'beat_task',
              'routing_key':'beat_task',
          }
  
  
      }
  }
  
  
  > 启动 beat 和 worker   （同时启动）
  
  celery -B -A apps worker -l INFO   #每隔五秒执行一次
  ```
  
  
  
  ### 实战  
  
  > 增量爬取 以及 定时爬取 
  
  * 增量 对单条数据操作 查询数据库 存在添加 不存在跳过   
  * pandas 全量对比 
  * 分页爬取   



## django 使用celery   

> pip install django==2.2.0
>
> pip install django-celery 
>
> pip install redis==2.10.6 



## flask 使用celery 

```
1.单独创建一个tasks.py  
from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task 
def send_mail(参数):
	操作  
	
views.py  

from tasks import send_mail
def 方法():
	send_mail(参数):
	
	
1.启动worker  
2.访问视图函数  


#encoding: utf-8

from celery import Celery
from flask_mail import Message
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)
mail.init_app(app)
alidayu.init_app(app)


# 运行本文件：
# 在windows操作系统上：
# celery -A tasks.celery worker --pool=solo --loglevel=info
# 在类*nix操作系统上：
# celery -A tasks.celery worker --loglevel=info

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)


@celery.task
def send_mail(subject,recipients,body):
    message = Message(subject=subject,recipients=recipients,body=body)
    mail.send(message)

@celery.task
def send_sms_captcha(telephone,captcha):
    alidayu.send_sms(telephone,code=captcha)
```

