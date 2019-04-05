#添加线程

#导入模块
import threading
#获取已激活的线程数
print(threading.active_count())
#1

#查看所有线程信息
print(threading.enumerate())
#[<_MainThread(MainThread, started 16520)>]

#查看现在正在运行的线程
print(threading.current_thread())
# <_MainThread(MainThread, started 16460)>

#添加线程， threading.Thread()  接收参数 target 代表这个线程 要完成的任务  需 自行定义
def thread_job():
    print("This is a thread of %s"%threading.current_thread())

def main():
    thread = threading.Thread(target=thread_job,)  #定义线程
    thread.start()       #让线程开始工作

if __name__=='__main__':
    main()
    # This is a thread of <Thread(Thread-1, started 16100)>



####不加 join 的结果
import time

def thread_job1():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)   #任务间隔 0.1s
    print("T1 finish\n")

added_thread = threading.Thread(target=thread_job1,name='T1')
# added_thread.start()
# print("all done\n")
# T1 start
# all done
#
#
# T1 finish

#加入join 的结果
#线程还未完成便输出 all done. 如果要遵循顺序 ，可以在启动线程后 对它  调用 join
added_thread.start()
added_thread.join()
print("all done\n")
# T1 start
#
# T1 finish
#
# all done

