import threading
import time


def work():
    time.sleep(1)
    thread=threading.current_thread()
    print(thread)

# 线程之间的执行顺序是无序的，由CPU调度决定某个线程执行
if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=work).start()
