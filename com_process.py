'''
进程间通信queue
'''
# from queue import Queue
import multiprocessing
from multiprocessing import Queue,Manager,Pipe,managers # 这个queue不能用于进程池,可以使用manage().Queue


# class pro(multiprocessing.Process):
#     def __init__(self,q):
#         super().__init__()
#         self.q = q
#     def run(self):
#         self.q.put('a')
# class cons(multiprocessing.Process):
#     def __init__(self,q):
#         super().__init__()
#         self.q = q
#     def run(self):
#         res = self.q.get()
#         print(res)

def pro(p):
    p.send('ss')

def cons(p):
    res = p.recv()
    print(res)

def add_va(m_dict,key,va):
    m_dict[key]=va
    print(m_dict)

    pass


if __name__ == "__main__":
    #queue
    # q= Manager().Queue(10)
    # process = multiprocessing.Pool(3)
    # p1 = process.apply_async(pro,args=(q,))
    # c1 = process.apply_async(cons,args=(q,))
    # process.close()
    # process.join()
    # print(c1.get())

    # p1 = pro(q)
    # c1 = cons(q)
    # p1.start()
    # c1.start()
    # p1.join()
    # c1.join()

    # pipe
    # recv_p,send_p=Pipe()  # 只能用于两个进程间的通信
    # p = multiprocessing.Process(target=pro,args=(recv_p,))
    # c = multiprocessing.Process(target=cons,args=(send_p,))
    # p.start()
    # c.start()
    # p.join()
    # c.join()
    # 共享内存
    manage_dict = Manager().dict()
    f_p1 = multiprocessing.Process(target=add_va,args=(manage_dict,'a1',1))
    f_p2 = multiprocessing.Process(target=add_va,args=(manage_dict,'a2',2))
    f_p1.start()
    f_p2.start()
    f_p1.join()
    f_p2.join()

   