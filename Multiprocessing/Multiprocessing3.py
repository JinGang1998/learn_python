#效率对比 threading & multiprocessing
#导入所需库
import multiprocessing as mp
#定义要实现的job
def job(q):
    res = 0
    for i in range(1000000):
        res += i+i**2+i**3
    q.put(res) #queue

#因为多进程是多核运算，所以我们将上节的多进程代码命名为multicore()
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:',res1+res2)

#创建多线程 multithread
import threading as td

def multithread():
    q = mp.Queue()  #thread 可放入 process  同样的queue 中
    t1 = td.Thread(target=job,args=(q,))
    t2 = td.Thread(target=job,args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:',res1+res2)

#创建普通函数
def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i+i**2+i**3
    print('normal:',res)

#运行时间
import time

if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print("normal time:",st1-st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time() - st2)
# 普通/多线程/多进程的运行时间分别是1.13，1.3和0.64秒。 我们发现
# 多核/多进程最快，说明在同时间运行了多个任务。 而多线程的运行时间
# 居然比什么都不做的程序还要慢一点，说明多线程还是有一定的短板的
# normal: 499999666667166666000000
# normal time: 1.6890830993652344
# multithread: 499999666667166666000000
# multithread time: 1.559133768081665
# multicore: 499999666667166666000000
# multicore time: 0.9694838523864746
