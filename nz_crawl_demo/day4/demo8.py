import threading
import random
import time
gMoney = 10000
gCondition = threading.Condition()

#生产者 消费者是多线程的一种模式

gTotalTimes = 10
gTime = 0

# 生产者
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        global gCondition
        while True:
            money= random.randint(1000,10000)
            gCondition.acquire() #上锁
            if gTime >= gTotalTimes:
                gCondition.release()
                break
            gMoney += money
            print("%s挣了%d元钱,余额%d元钱" % (threading.current_thread(),money,gMoney))
            gTime +=1
            time.sleep(0.5)
            gCondition.notify_all()
            gCondition.release() #释放锁

#消费者
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        global gCondition
        while True:
            money = random.randint(1000,10000)
            gCondition.acquire()
            while gMoney < money:
                if gTime >= gTotalTimes:
                    gCondition.release()
                    return
                print("%s消费了%d元钱,余额%d元钱,余额不足" % (threading.current_thread(), money, gMoney))
                gCondition.wait() #阻塞等待
            gMoney -= money
            print("%s消费了%d元钱,余额%d元钱" % (threading.current_thread(), money, gMoney))
            time.sleep(0.5)
            gCondition.release()

def main():

    for x in range(3):
        t = Consumer(name="消费者线程%d" % x)
        t.start()

    for x in range(3):
        t = Producer(name="生产者线程%d" % x)
        t.start()

if __name__ == "__main__":
    main()