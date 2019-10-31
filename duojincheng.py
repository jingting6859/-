import multiprocessing
a = 0
def add(a):
    # global a
    a += 1
    print(a)
    return a
def desc():
    global a
    a -= 1

if __name__ == "__main__":
    # p1 = multiprocessing.Process(target=add)
    # # p1 = multiprocessing.Process(target=add)
    # p2 = multiprocessing.Process(target=desc)
    # p1.start()
 
    # p1.join()
    # print(a)
    # p2.start()
    # p2.join()
    # print(a)
    p = multiprocessing.Pool(multiprocessing.cpu_count())
    # res = p.apply_async(add)
    # p.close()
    # p.join()
    # print(res.get())
    
    for i in p.imap_unordered(add,[1,3,2]):
        print(i)
    