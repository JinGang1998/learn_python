#GIL不一定有效率

# #
#
#     尽管Python完全支持多线程编程， 但是解释器的C语言实现部分在完全并行执行时并不是线程安全的。 实际
# 上，解释器被一个全局解释器锁保护着，它确保任何时候都只有一个Python线程执行。 GIL最大的问题就是Python
# 的多线程程序并不能利用多核CPU的优势 （比如一个使用了多个线程的计算密集型程序只会在一个单CPU上面运行）。
#
#     在讨论普通的GIL之前，有一点要强调的是GIL只会影响到那些严重依赖CPU的程序（比如计算型的）。 如果你的程
# 序大部分只会涉及到I/O，比如网络交互，那么使用多线程就很合适， 因为它们大部分时间都在等待。实际上，你完全可以放
# 心的创建几千个Python线程， 现代操作系统运行这么多线程没有任何压力，没啥可担心的。
#

#测试 GIL

import threading
from queue import Queue
import copy
import time

def job(l,q):
    res = sum(l)
    q.put(res) #Queue.get([block[, timeout]])   读队列，timeout等待时间
       # Queue.put(item, [block[, timeout]])   写队列，timeout等待时间

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job,args=(copy.copy(l),q),name='T%i'%i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal:',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading:',time.time()-s_t)
# 1999998000000
# normal: 0.1799166202545166
# 1999998000000
# multithreading: 0.16989755630493164
# 如果你成功运行整套程序, 你大概会有这样的输出. 我们的运算结果没错, 所以程序
#  threading 和 Normal 运行了一样多次的运算. 但是我们发现 threading 却没有快多少,
#  按理来说, 我们预期会要快3-4倍, 因为有建立4个线程, 但是并没有. 这就是其中的 GIL 在作怪.
