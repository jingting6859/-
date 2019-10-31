import threading,time
'''
信号量threading.semaphore 是用于控制进入数量的锁，
控制同时进行的线程，内部是基于Condition来进行实现的

'''
class htmlSpider(threading.Thread):
    def __init__(self,url,sem):
        super().__init__()
        self.sem=sem
        self.url=url
    def run(self):
        print('sucess')
        time.sleep(1)
        self.sem.release()

class urlpro(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem=sem
    def run(self):
        for i in range(10):
            self.sem.acquire()
            t = htmlSpider("https://baidu.com/{}".format(i), self.sem)
            t.start()
if __name__ == "__main__":
    sem = threading.Semaphore(2)
    u = urlpro(sem)
    u.start()

    