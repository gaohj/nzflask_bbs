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

  

  

  

  