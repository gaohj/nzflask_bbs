
from apps import app

# @app.task(queue='task2_add3')
@app.task
def add3(x,y):
    print(x-y)
    return x-y