import multiprocessing
import time


def work():
    for i in range(20):
        print("子进程工作中。。。")
        time.sleep(0.5)

if __name__ == '__main__':
    process_work = multiprocessing.Process(target=work)
    # 设置守护主进程，当主进程结束后，子进程也会立马结束
    process_work.daemon = True
    process_work.start()

    time.sleep(1)
    print("主进程执行完成！")