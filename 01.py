import threading,time
def run(num):
    print('当前线程是%s'%threading.currentThread().name)
    print(num)
    time.sleep(2)
    print('%s线程结束'%threading.currentThread().name)

if __name__ == "__main__":
    print(threading.currentThread().name + '开始')
    t1 = threading.Thread(target=run,name='run1',args=(1,))
    t2 = threading.Thread(target=run,name='run2',args=(1,))
    t1.start()
    t2.start()
    t1.join()
    print('结束')
