import threading,time
'''
Event python线程的事件用于主线程控制其他线程的执行，事件主要提供了三个方法wait、clear、set

事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，如果“Flag”值为True，那么event.wait 方法时便不再阻塞。

clear：将“Flag”设置为False
set：将“Flag”设置为True
'''
class Light(threading.Thread):
    def __init__(self,e):
        super().__init__()
        self.count=0
        self.e=e
    def run(self):
        while True:
            if self.count <= 5:
                self.e.set()
            elif self.count>10:
                self.count = 0
            else:
                self.e.clear()
            self.count += 1
class car(threading.Thread):
    def __init__(self,e,name):
        super().__init__()
        self.e=e
        self.name=name
    def run(self):
        while True:
            if self.e.is_set():
                print(self.name+'绿灯行')
                time.sleep(1)
                
            else:
                print(self.name + '红灯停')
                time.sleep(1)
                self.e.wait()
                print('[绿灯。。。。。。。。。。。。。。。。。]')


if __name__ == "__main__":
    e = threading.Event()
    l = Light(e)
    l.start()
    c1 = car(e,'car1')
    c2 = car(e,'car2')
    c3 = car(e,'car3')
    c1.start()
    c2.start()
    c3.start()
    l.join()
    c1.join()
    c2.join()
    c3.join()