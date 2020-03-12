import time
import threading
class DrivingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('%s正在开车' % threading.current_thread())  # 当前线程
            time.sleep(2)

class LolingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('%s正在撸' % threading.current_thread()) #当前线程
            time.sleep(2)


def main():
    t1 = DrivingThread() #实例化线程 并且制定要做什么
    t2 = LolingThread()

    t1.start()
    t2.start()
    print(threading.enumerate()) #查看线程的数量
if __name__ == "__main__":
    main()