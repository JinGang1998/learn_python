# 多进程 Multiprocessing 和多线程 threading 类似, 他们都是在
#  python 中用来并行运算的. 不过既然有了 threading, 为什么 Python
# 还要出一个 multiprocessing 呢? 原因很简单, 就是用来弥补 threading 的一些劣势,
#  比如在 threading 教程中提到的GIL.

#导入线程进程标准模块
import multiprocessing as mp
import threading as td

#定义一个被线程和进程调用的函数
def job(a,d):
    print('aaaaaaa')


# #创建线程和进程
# t1 = td.Thread(target=job,args=(1,2))
# p1 = mp.Process(target=job,args=(1,2))
#
# #分别启动线程和进程
# t1.start()
# p1.start()
#
# #分别连接线程和进程
# t1.join()
# p1.join()

#在运用时 需要添加上 定义main函数的语句

if __name__ == '__main__':
    p1 = mp.Process(target=job,args=(1,2))
    p1.start()
    p1.join()
