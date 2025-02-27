import threading
import time


def sing():
    for i in range(3):
        print("唱歌。。。")
        time.sleep(1)


def dance():
    for i in range(3):
        print("跳舞。。。")
        time.sleep(1)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)
    sing_thread.start()
    dance_thread.start()
