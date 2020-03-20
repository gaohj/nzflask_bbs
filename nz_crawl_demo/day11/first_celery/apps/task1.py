from apps import app

@app.task()
def add(x,y):
    print(x+y)
    return x+y
@app.task()
def add2(x,y):
    print(x*y)
    return x*y
