from apps import app
import time

@app.task
def beat_task(x,y,name):
    # time.sleep(5)
    print(x+y)
    print(name)
    return 'hello celery beat'
