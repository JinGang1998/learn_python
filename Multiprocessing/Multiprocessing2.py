import multiprocessing as mp
#
#定义一个被多线程调用的函数，q 就像一个队列， 用来保存每次函数运行的结果
#该函数 没有返回值
def job(q):
    res = 0
    for i in range(1000):
        res += i+i**2+i**3
    q.put(res)   #queue

#定义一个多线程队列，用来存储结果
if __name__ == '__main__':
    q = mp.Queue()
    #定义两个线程函数，用来处理同一个任务
    p1 = mp.Process(target=job,args=(q,))#args 的参数只要一个值的时候，参数后面需要加一个逗号，表示args是可迭代的，后面可能还有别的参数，不加逗号会出错
    p2 = mp.Process(target=job,args=(q,))
    #分别启动、连接两个线程
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    #上面是分批处理的，所以这里分两批输出，将结果分别保存
    res1 = q.get()
    res2 = q.get()
    #打印最后的运算结果
    print(res1+res2)
