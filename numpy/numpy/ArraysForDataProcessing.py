# NumPy数组使你可以将许多种数据处理任务表述为简洁的数组表达式（否则需要编写循环）。用数组表达式代替循环的做法，通常被称为矢量化。

import numpy as np

# np.meshgrid函数接受两个一维数组，并产生两个二维矩阵（对应于两个数组中所有的(x,y)对）
# 要在一组值（网格型）上计算函数 √x2+y2。
points = np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
print(ys)

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

import matplotlib.pyplot as plt
plt.imshow(z,cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
#plt.show()


#将条件逻辑表述为数组运算
# numpy.where函数是三元表达式x if condition else y的矢量化版本

xarr = np.array([1.1,1.2,1.3,1.4,1.5])
yarr = np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True,False,True,True,False])

result = [(x if c else y)
          for x,y,c in zip(xarr,yarr,cond)]
print(result)

result = np.where(cond,xarr,yarr)
print(result)


# np.where的第二个和第三个参数不必是数组，它们都可以是标量值。在
# 数据分析工作中，where通常用于根据另一个数组而产生一个新的数组。
# 假设有一个由随机数据组成的矩阵，你希望将所有正值替换为2，将所有负值替换为－2。
arr = np.random.randn(4,4)
print(arr)
print(arr > 0)
print(np.where(arr > 0,2,-2))

# 使用np.where，可以将标量和数组结合起来。例如，我可用常数2替换arr中所有正的值
print(np.where(arr > 0,2,arr))
# 传递给where的数组大小可以不相等，甚至可以是标量值。


#数学和统计方法
# sum、mean以及标准差std等聚合计算（aggregation，
# 通常叫做约简（reduction））既可以当做数组的实例方法调用，也可以当做
# 顶级NumPy函数使用。
arr = np.random.randn(5,4)
print(arr)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())

# mean和sum这类的函数可以接受一个axis选项参数，用于计算
# 该轴向上的统计值，最终结果是一个少一维的数组
print(arr.mean(axis=1))
print(arr.sum(axis=0))
# ，arr.mean(1)是“计算行的平均值”，arr.sum(0)是“计算每列的和”。

# cumsum和cumprod之类的方法则不聚合，而是产生一个由中间结果组成的数组
arr = np.array([0,1,2,3,4,5,6,7])
print(arr.cumsum())

# 在多维数组中，累加函数（如cumsum）返回的是同样大小的数组，但是会根据每个低维的切片沿着标记轴计算部分聚类
arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(arr)
print(arr.cumsum(axis=0))
print(arr.cumprod(axis=1))


#列出了全部的基本数组统计方法
# 在上面这些方法中，布尔值会被强制转换为1（True）和0（False）。因此，sum经常被用来对布尔型数组中的True值计数
arr = np.random.randn(100)
print((arr > 0).sum())

# 另外还有两个方法any和all，它们对布尔型数组非常有用。any用于测试数
# 组中是否存在一个或多个True，而all则检查数组中所有值是否都是True
bools = np.array([False,False,True,True])
print(bools.any())
print(bools.all())
# 这两个方法也能用于非布尔型数组，所有非0元素将会被当做True。

#                             速度
#排序   quicksort (快速排序)  1
#  mergesort(归并排序)           2
#  heapsort(堆排序 ）           3


# sort()函数返回输入数组的排序副本。 它有以下参数：
#
# numpy.sort(a, axis, kind, order)
# 1 	a 要排序的数组
# 2 	axis 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序
# 3 	kind 默认为'quicksort'(快速排序)
# # 4 	order 如果数组包含字段，则是要排序的字段

a = np.array([[3,7],[9,1]])
print('我们的数组是：')
print(a)
print('\n')
print('调用sort()函数：')
print(np.sort(a))
print('\n')
print('沿轴 0 排序：')
print(np.sort(a,axis=0))
print('\n')
#在sort函数中排序字段
dt = np.dtype([('name','S10'),('age',int)])
a = np.array([("raju",21),("anil",25),("ravi",17),("amar",27)],dtype=dt)
print("我们的数组是：")
print(a)
print('\n')
print('按name排序：')
print(np.sort(a,order='name'))


# numpy.argsort()函数对输入数组沿给定轴执行间接排序，
# 并使用指定排序类型返回数据的索引数组。 这个索引数组
# 用于构造排序后的数组。
arr = np.random.randn(5,3)
print(arr)
arr.sort(1)
print(arr)

x = np.array([3,1,2])
print('我们的数组是：')
print(x)
print('\n')
print('对x调用argsort()函数：')
y = np.argsort(x)
print(y)
print('\n')
print('以排序后的顺序重构原数组：')
print(x[y])
print('\n')
print('使用循环重构原数组: ')
for i in y:
    print(x[i])


#numpy.lexsort()
# 函数使用键序列执行间接排序。 键可以看作是电子表格中的一列。 该函
# 数返回一个索引数组，使用它可以获得排序数据。 注意，最后一个键恰好
# 是 sort 的主键。

nm = ('raju','anil','ravi','amar')
dv = ('f.y.','s.y.','s.y.','f.y.')
ind = np.lexsort((dv,nm))
print('调用lexsort()函数：')
print(ind)
print('\n')
print('使用这个索引来获取排序后的数据：')
print([nm[i] + "," + dv[i] for i in ind])


#唯一化以及它的集合逻辑
# 一些针对一维ndarray的基本集合运算。最常用的可能要数np.unique了，它用于找出数组中的唯一值并返回已排序的结果
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
print(np.unique(names))
ints = np.array([3,3,3,2,2,1,1,4,4])
print(np.unique(ints))

# 拿跟np.unique等价的纯Python代码来对比一下
print(sorted(set(names)))

# 一个函数np.in1d用于测试一个数组中的值在另一个数组中的成员资格，返回一个布尔型数组
values = np.array([6,0,0,3,2,5,6])

print(np.in1d(values,[2,3,6]))
