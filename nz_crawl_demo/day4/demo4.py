import time
import threading
def driving():
    for x in range(3):
        print('%s正在开车' % threading.current_thread()) #当前线程
        time.sleep(2)


def loling():
    for x in range(3):
        print('%s正在撸' % threading.current_thread()) #当前线程
        time.sleep(2)


def main():
    t1 = threading.Thread(target=driving) #实例化线程 并且制定要做什么
    t2 = threading.Thread(target=loling)

    t1.start()
    t2.start()
    print(threading.enumerate()) #查看进程的数量
if __name__ == "__main__":
    main()