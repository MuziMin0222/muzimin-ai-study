import multiprocessing
import os
import time


def sing(num, name):
    print("sing进程的父进程：", os.getppid())
    print("sing进程的ID：", os.getpid())
    for i in range(num):
        print("唱歌。。。" + name)
        time.sleep(0.5)


def dance(num, name):
    print("dance进程的父进程：", os.getppid())
    print("dance进程的ID：", os.getpid())
    for i in range(num):
        print("跳舞。。。" + name)
        time.sleep(0.5)


if __name__ == '__main__':
    print("main进程的父进程：", os.getppid())
    print("main进程的ID：", os.getpid())
    sing_process = multiprocessing.Process(target=sing, args=(2, "muzimin",))
    dance_process = multiprocessing.Process(target=dance, kwargs={"name": "Lhm", "num": 3})

    sing_process.start()
    dance_process.start()
