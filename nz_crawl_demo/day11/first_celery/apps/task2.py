
from apps import app

@app.task()
def add3(x,y):
    print(x-y)
    return x-y