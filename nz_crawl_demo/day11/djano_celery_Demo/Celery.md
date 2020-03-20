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
  
  
  
  from datetime import timedelta
  from celery.schedules import crontab
  CELERYBEAT_SCHEDULE = {
      'python1904':{
          'task':'apps.beat_task.beat_task',#要执行的任务的名字
          'schedule':timedelta(seconds=5),#要执行的任务的名字
          'args':(5,8),
          'kwargs':{'name':'kangbazi'},
          'options':{
              'queue':'beat_task',
              'routing_key':'beat_task',
          }
  
  
      }
  }
  ```
  
  
  
  