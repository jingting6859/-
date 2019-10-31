'''
线程池
'''

from concurrent import futures
from concurrent.futures import ThreadPoolExecutor,as_completed,Future
import time
def run_time(times):
    time.sleep(times)
    print("{}执行".format(times))
    time.sleep(1)
    return times


times=[1,2,3,4]
executor = ThreadPoolExecutor(max_workers=2)
# tasks = [executor.submit(run_time,url) for url in times]
# for fu in as_completed(tasks):
#     print(fu.result())
# task1 = executor.submit(run_time,1)
# task2 = executor.submit(run_time,2)
# print(task1.done())  #任务是否执行完成
# print(task1.result()) #任务返回值
for data in as_completed(executor.map(run_time,times)):
    pass