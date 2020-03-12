#共享全局变量 线程是无序的  容易造成 数据的错误
#为了避免 上锁
import threading

VALUE = 0
gLock = threading.Lock()

def add_value():
    global VALUE
    gLock.acquire()
    for x in range(10000000):
        VALUE +=1
    gLock.release()
    print("value:%d" % VALUE)

def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == "__main__":
     main()
