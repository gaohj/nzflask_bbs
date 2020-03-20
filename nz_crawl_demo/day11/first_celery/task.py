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
