import multiprocessing
import time


def sing(num, name):
    for i in range(num):
        print("唱歌。。。" + name)
        time.sleep(0.5)


def dance(num, name):
    for i in range(num):
        print("跳舞。。。" + name)
        time.sleep(0.5)


if __name__ == '__main__':
    # args: 使用元组的方式给指定的任务传参，元组的顺序就是任务的参数顺序
    #     元组的方式传参一定要和参数的顺序保持一致
    #     如果元组中的个数只有1个，那么后面必须带有逗号，如果多于1个，逗号可以不带
    # kwargs: 使用字典的方式进行传参，key的名就是参数的名字
    #     字典方式传参中的key一定要和参数名保持一致
    sing_process = multiprocessing.Process(target=sing, args=(2, "muzimin",))
    dance_process = multiprocessing.Process(target=dance, kwargs={"name": "Lhm", "num": 3})

    sing_process.start()
    dance_process.start()
