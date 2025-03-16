import threading

g_num = 0


def sum1():
    # 上锁
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1

    # 解锁
    mutex.release()

    print(g_num)


def sum2():
    # 上锁
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1

    # 解锁
    mutex.release()

    print(g_num)


if __name__ == '__main__':
    mutex = threading.Lock()

    thread1 = threading.Thread(target=sum1)
    thread2 = threading.Thread(target=sum2)

    thread1.start()
    thread2.start()
