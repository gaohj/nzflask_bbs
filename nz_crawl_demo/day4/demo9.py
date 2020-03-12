from queue import Queue

import threading
import time
# q = Queue(4) 4表示最多4个
#
# for x in range(4):
#     q.put(x)
#
# for x in  range(4):
#     print(q.get())

# print(q.qsize())





def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1 
        time.sleep(1)

def get_value(q):
    while True:
        print(q.get())

def main():
    q = Queue(4)

    t1 = threading.Thread(target=set_value,args=[q])
    t2 = threading.Thread(target=get_value,args=[q])

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()