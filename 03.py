import threading,time
'''
继承方式创建多线程
'''
num = 0
class testThread(threading.Thread):
    # 重写run 方法
    def __init__(self,n):
        super().__init__()
        self.n = n
    def run(self):
        global num
        print(threading.currentThread().name)
        # print(self.n)
        for i in range(1000):
            num += self.n
            # print(num)
            time.sleep(1)
            num -= self.n
            print(num)
        print('子线程结束')

if __name__ == "__main__":
    t1 = testThread(5)
    t2 = testThread(7)
    t1.start()
    t2.start()
    t1.join()
    t2.join()