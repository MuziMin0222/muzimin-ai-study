import threading
import time


def work():
    for i in range(20):
        print("子进程工作中。。。")
        time.sleep(0.5)


if __name__ == '__main__':
    # 设置守护主进程，当主线程结束后，子线程也会立马结束

    # 方式一：
    # threading.Thread(target=work, daemon=True).start()

    # 方式二
    sub_thread = threading.Thread(target=work)
    sub_thread.setDaemon(True)
    sub_thread.start()
    time.sleep(1)
    print("主进程执行完成！")
