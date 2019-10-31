'''
多进程与多线程的应用
多进程应用在耗cpu的情况下，多线程应用在IO操作比较频繁的情况下，
多进程切换耗时，耗资源，尽量使用多线程
'''
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,as_completed
import time
# 计算型比较：
def fib(n):
    if n<2:
        return 1
    return fib(n-1)+fib(n-2)

def IO_xing(n):
    time.sleep(n)
    return n
if __name__ == "__main__":
    # tasks = [ThreadPoolExecutor(3).submit(IO_xing,num) for num in [2]*20]
    # start = time.time()
    # for fu in as_completed(tasks):
    #     print(fu.result())
    # end = time.time()-start
    # print(end) #多线程17.30


    tasks = [ProcessPoolExecutor(3).submit(IO_xing,num) for num in [2]*20]
    start = time.time()
    for fu in as_completed(tasks):
        print(fu.result())
    end = time.time()-start
    print(end) #多进程1.635
