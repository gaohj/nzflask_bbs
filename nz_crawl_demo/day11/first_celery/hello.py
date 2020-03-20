#导入任务
from task import hello,sums
from apps.task1 import add,add2
from apps.task2 import add3

if __name__ == "__main__":
    # hello.delay('world')
    # sums.delay(5,10)
    add.delay(10,20)
    add2.delay(30,40)
    add3.delay(50,15)

