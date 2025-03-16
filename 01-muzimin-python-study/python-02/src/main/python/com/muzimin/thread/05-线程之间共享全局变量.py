import threading
import time

my_list = []


def write():
    for i in range(5):
        my_list.append(i)
    print(my_list)


def read():
    print(my_list)


if __name__ == '__main__':
    threading.Thread(target=write).start()
    time.sleep(1)
    threading.Thread(target=read).start()
