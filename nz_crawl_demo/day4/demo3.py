import time

def driving():
    for x in range(3):
        print('%s正在开车' % x)
        time.sleep(2)


def loling():
    for x in range(3):
        print('%s正在撸' % x)
        time.sleep(2)


def main():
    driving()
    loling()

if __name__ == "__main__":
    main()