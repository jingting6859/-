import threading,time
from threading import Thread
'''
多线程对同一数据进行操作，实现高并发
'''
lock=threading.Lock()
num = 0
def run(n):
    global num
    with lock:
        print(threading.currentThread().name)
        print('n=%d'%n)
        for i in range(10):
            num = num + n
            time.sleep(1)
            num = num - n
            print(num)
    print('子线程结束')

if __name__ == "__main__":
    # print('主线程开始')
    t1 = threading.Thread(target=run,name='t1',args=(1,))
    t2 = threading.Thread(target=run,name='t2',args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)

