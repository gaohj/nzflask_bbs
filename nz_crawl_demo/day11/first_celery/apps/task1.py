from apps import app

@app.task()
def add(x,y,name):
    print("你好:%s" % name )
    return x+y
# @app.task(queue='task1_add2')
@app.task
def add2(x,y):
    print(x*y)
    return x*y
