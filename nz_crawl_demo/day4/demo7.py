import threading
import random
import time
gMoney = 10000
gLock = threading.Lock()

gTotalTimes = 10
gTime = 0

# 生产者
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            money= random.randint(1000,10000)
            gLock.acquire() #上锁
            if gTime >= gTotalTimes:
                gLock.release()
                break
            gMoney += money
            print("%s挣了%d元钱,余额%d元钱" % (threading.current_thread(),money,gMoney))
            gTime +=1
            gLock.release() #释放锁
            time.sleep(0.5)
#消费者
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(1000,10000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print("%s消费了%d元钱,余额%d元钱" % (threading.current_thread(), money, gMoney))
            else:
                if gTime >= gTotalTimes:
                    gLock.release()
                    break
                print("%s消费了%d元钱,余额%d元钱,余额不足" % (threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(0.5)

def main():

    for x in range(3):
        t = Consumer(name="消费者线程%d" % x)
        t.start()

    for x in range(3):
        t = Producer(name="生产者线程%d" % x)
        t.start()

if __name__ == "__main__":
    main()