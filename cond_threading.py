import threading,time,random
'''
条件锁threading.condtion
消费者小于0，等待唤醒
'''
L = []
class proThread(threading.Thread):
    # 重写run 方法
    def __init__(self,con,name):
        super().__init__()
        self.con =con
        self.name=name
    def run(self):
        global L
        while True:
            v= random.randint(0,100)
            if self.con.acquire():
                print('%s线程'%self.name)
                L.append(v)
                self.con.notify()
                print('生产者',self.name,'append'+str(L[0]),L)
                self.con.release()
            time.sleep(3)
            
        print('子线程结束')

class consuThread(threading.Thread):
    # 重写run 方法
    def __init__(self,con,name):
        super().__init__()
        self.con =con
        self.name=name
    def run(self):
        global L
        while True:
            if self.con.acquire():
                print('%s线程'%self.name)
                if len(L)==0:
                    print('消费者等待中')
                    self.con.wait()
                P = L.pop(0)
                print('消费者',self.name,'Delete'+str(P),L)
                self.con.release()
            time.sleep(1)
            
        print('子线程结束')
if __name__ == "__main__":
    con = threading.Condition()
    p1 = proThread(con,'生产者1')
    p2 = proThread(con,'生产者2')
    c1 = consuThread(con,'消费者1')
    c2 = consuThread(con,'消费者2')
    c3 = consuThread(con,'消费者3')
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    c3.start()
    p1.join()
    p2.join()
    c1.join()
    c2.join()
    c3.join()
    print(num)


# import threading,time
# from random import randint
# class Producer(threading.Thread):
#     def run(self):
#         global L
#         while True:
#             val=randint(0,100)
#             # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#             print('生产者',self.name,' Append'+str(val),L)
#             if lock_con.acquire():
#                 L.append(val)
#                 lock_con.notify()
#                 lock_con.release()
#             time.sleep(3)
# class Consumer(threading.Thread):
#     def run(self):
#         global L
#         while True:
#             lock_con.acquire()
#             if len(L)==0:
#                 lock_con.wait()
#             print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#             print('消费者',self.name,'Delete'+str(L[0]),L)
#             del L[0]
#             lock_con.release()
#             time.sleep(0.5)
# if __name__=='__main__':
#     L=[]
#     lock_con=threading.Condition()
#     threads=[]
#     for i in range(5):
#         threads.append(Producer())
#     threads.append(Consumer())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()