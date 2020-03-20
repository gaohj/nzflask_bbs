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
  4. 消费者  worker （task consumer）可以有多个 
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
celery worker -A celery_app名称 -I INFO
  celery worker -A task -I INFO
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
  
  
  
  
  
  