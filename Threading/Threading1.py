# 使用join 对 控制多个线程 的执行顺序 非常关键 。
import threading
import time
def T1_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():
    print("T2 start\n")
    print("T2 finish\n")

thread_1 = threading.Thread(target=T1_job,name='T1')
thread_2 = threading.Thread(target=T2_job,name='T2')
# thread_1.start() #开启 T1
# thread_2.start()  #开启 T2
# print("all done\n")
# T1 start
#
# T2 start
#
# T2 finish
#
# all done
#
# T1 finish


# 现在T1和T2都没有join，注意这里说”一种”是因为all done的出现完全取决于两个线程的执行速度，
#  完全有可能T2 finish出现在all done之后。这种杂乱的执行方式是我们不能忍受的，因此要使用join加以控制。
# thread_1.start()
# thread_1.join()   # notice the  difference
# thread_2.start()
# print("all done\n")
# T1 start
#
# T1 finish
#
# T2 start
#
# T2 finish
#
# all done   T2  在T1 结束后才 执行

# thread_1.start()
# thread_2.start()
# thread_1.join()  #notice the difference
# print("all done\n")
# T1 start
#
# T2 start
#
# T2 finish
#
# T1 finish
#
# all done

thread_1.start()
thread_2.start()
thread_2.join()
thread_1.join()
print("all done\n")
# T1 start
#
# T2 start
#
# T2 finish
#
# T1 finish
#
# all done
