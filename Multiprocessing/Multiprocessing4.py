#进程池 Pool
import multiprocessing as mp

def job(x):
    return x*x

#进程池Pool()  和 map()

#定义一个Pool
#pool = mp.Pool()
# 有了池子之后，就可以让池子对应某一个函数，我们向池子里丢数据，池子就会返回
# 函数返回的值。 Pool和之前的Process的不同点是丢向Pool的函数有返回值，而Process的
# 没有返回值。

# 接下来用map()获取结果，在map()中需要放入函数和需要迭代运算的值，
# 然后它会自动分配给CPU核，返回结果
#res = pool.map(job,range(10))

# 将其放在函数中运行一下
def multicore():
    # pool = mp.Pool()
    # 自定义核数量
    pool = mp.Pool(processes=3)  #定义CPU核数量为3
    res = pool.map(job,range(10))
    print(res)
    # Pool除了map()外，还有可以返回结果的方式，那就是apply_async().
    res = pool.apply_async(job,(2,))
    #用get 获得结果
    print(res.get())
    #迭代器，i=0 时 apply 一次，i=1时 apply 一次 等等
    multi_res = [pool.apply_async(job,(i,)) for i in range(10)]
    #从迭代器中取出
    print([res.get() for res in multi_res])
if __name__ == '__main__':
    multicore()
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
#     Pool默认调用是CPU的核数，传入processes参数可自定义CPU核数
#     map() 放入迭代参数，返回多个结果
#
#     apply_async()只能放入一组参数，并返回一个结果，如果想得到map()的效果需要通过迭代

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 4
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
