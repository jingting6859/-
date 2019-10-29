import threading,time
'''
互斥锁 threading.Lock()
'''
num = 0
class testThread(threading.Thread):
    # 重写run 方法
    def __init__(self,lock,n):
        super().__init__()
        self.n = n
        self.lock=lock
    def run(self):
        global num
        print(threading.currentThread().name)
        # print(self.n)
        for i in range(1000):
            while self.lock.acquire():
                num += self.n
                # print(num)
                time.sleep(1)
                num -= self.n
                print(num)
                self.lock.release()
        print('子线程结束')

if __name__ == "__main__":
    lock = threading.Lock()
    t1 = testThread(lock,5)
    t2 = testThread(lock,7)
    t1.start()
    t2.start()
    t1.join()
    t2.join()