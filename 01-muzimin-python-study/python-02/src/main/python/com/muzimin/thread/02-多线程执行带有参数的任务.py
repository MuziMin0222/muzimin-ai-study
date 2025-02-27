import threading
import time


def sing(num):
    for i in range(num):
        print("唱歌。。。")
        time.sleep(1)


def dance(count):
    for i in range(count):
        print("跳舞。。。")
        time.sleep(1)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing, args=(3,))
    dance_thread = threading.Thread(target=dance, kwargs={"count": 2})
    sing_thread.start()
    dance_thread.start()
