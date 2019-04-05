import numpy as np
import time

#numpy之于数值计算的重要原因之一是因为它可以高效处理大量数组的数据
my_arr = np.arange(1000000)
my_list = list(range(1000000))
a1 = time.clock()
for _ in range(10):
    my_arr2 = my_arr * 2
a2 = time.clock()

print(a2 - a1)  #0.030668269999999997

a3 = time.clock()
for _ in range(10):
    my_list2 = [x * 2 for x in my_list]

a4 = time.clock()

print(a4-a3)   #1.04504897  慢了将近100倍

#Generate some random data
data = np.random.randn(2,3)
print(data)

print('data * 10: \n',data * 10)

print('data + data : \n',data+data)

print('data shape:',data.shape)


#创建ndarray
data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
print(arr1)
#嵌套序列 被转换为多维数组
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr1.dtype)
print(arr2.dtype)
print(np.zeros(10))
print(np.zeros((3,6)))
print(np.empty((2,3,2)))
#认为np.empty会返回全0数组的想法是不安全的。很多情况下（如前所示），它返回的都是一些未初始化的垃圾值。
print(np.arange(15))

#如果没有特别指定，数据类型基本都是float64（浮点数）

arr1 = np.array([1,2,3],dtype=np.float64)
arr2 = np.array([1,2,3],dtype=np.int32)

print(arr1)
print(arr2)

arr = np.array([1,2,3,4,5])
print(arr.dtype)

float_arr = arr.astype(np.float64)
print(float_arr.dtype)
#整数被转换成了浮点数。如果将浮点数转换成整数，则小数部分将会被截取删除：

numeric_strings = np.array(['1.25','-9.6','42'],dtype=np.string_)
print(numeric_strings.astype(float))

int_array = np.arange(10)
calibers = np.array([.22,.270,.357,.380,.44,.50],dtype=np.float64)
print(int_array.astype(calibers.dtype))

empty_uint32 = np.empty(8,dtype='u4')
print(empty_uint32)
print(empty_uint32.dtype)

arr = np.array([[1.,2.,3.,],[4.,5.,6.]])
print(arr)
print(arr*arr)
print(arr-arr)

#数组与标量的算术运算会将标量值传播到各个元素
print(1/arr)
print(arr * 0.5)

arr2 = np.array([[0.,4.,1.],[7.,2.,12.]])
print(arr2)
print(arr2>arr)

#数组的广播
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = np.array([1.0,2.0,3.0])
print('第一个数组：')
print(a)
print('\n第二个数组：')
print(b)
print('\n第一个数组加第二个数组：')
print(a + b)


#基本的索引和切片
arr = np.arange(10)

print(arr)
print(arr[5])
print(arr[5:8])

arr[5:8] = 12
print(arr)

arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
print(arr)
arr_slice[:] = 64
print(arr)

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d[2])

print(arr2d[0][2])
print(arr2d[0,2])

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d[0])
#将arr3d[0]的数据进行备份
old_values = arr3d[0].copy()
#修改arr3d[0]的值为42
arr3d[0] = 42
print(arr3d)
print('==============分割线================')
arr3d[0] = old_values
print(arr3d)

print(arr3d[1,0])
print('============分割线============')
x = arr3d[1]
print(x)
print(x[0])


#切片索引
print(arr)
print(arr[1:6])

print(arr2d)
print('===============分割线===============')
print(arr2d[:2])

print(arr2d[:2,1:])
print(arr2d[1,:2])
print(arr2d[:2,2])

print(arr2d[:,:1])


#布尔型索引
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data = np.random.randn(7,4)

print(names)
print(data)

print(names=='Bob')
#[ True False False  True False False False]
print(data[names=='Bob'])


print(data[names == 'Bob',2:])
print('==========分割线==========')
print(data[names=='Bob',3])
#选择除’Bob‘以外的其他值   ~用来表示对条件的否定
print(names != 'Bob')
print(data[~(names=='Bob')])

cond = names =='Bob'
print(data[~cond])
#使用 &（和）  、  |（或）之类的布尔运算符
mask = (names == 'Bob') | (names == 'Will')
print(mask)
print(data[mask])
#过布尔型索引选取数组中的数据，将总是创建数据的副本

# 通过布尔型数组设置值是一种经常用到的手段。为了将data中的所有负值都设置为0
data[data<0] = 0
print(data)

data[names != 'Joe'] = 7
print(data)


#花式索引  -> 利用整数数组进行索引
arr = np.empty((8,4))
for i in range(8):
    arr[i] = i
print(arr)

# 为了以特定顺序选取行子集，只需传入一个用于指定顺序的整数列表或ndarray
print(arr[[4,3,0,6]])

# 使用负数索引将会从末尾开始选取行
print(arr[[-3,-5,-7]])

# 一次传入多个索引数组会有一点特别。它返回的是一个一维数组，其中的元素对应各个索引元组
arr = np.arange(32).reshape((8,4))
print(arr)
print(arr[[1,5,7,2],[0,3,1,2]])
# 无论数组是多少维的，花式索引总是一维的

print(arr[[1,5,7,2]][:,[0,3,1,2]])
# 花式索引跟切片不一样，它总是将数据复制到新数组中


#数组转置和轴对称
arr = np.arange(15).reshape((3,5))
print(arr)
print(arr.T)      #转置

arr = np.random.randn(6,3)
print(arr)
print(np.dot(arr.T,arr))      #np.dot计算矩阵内积

# 对于高维数组，transpose需要得到一个由轴编号组成的元组才能对这些轴进行转置
arr = np.arange(16).reshape((2,2,4))
print(arr)
print('============分割线===============')
print(arr.transpose((1,0,2)))

# 简单的转置可以使用.T，它其实就是进行轴对换而已。ndarray还有一个swapaxes方法，它需要接受一对轴编号
print(arr)
print('============分割线=============')
print(arr.swapaxes(1,2))
# swapaxes也是返回源数据的视图（不会进行任何复制操作）

