#pandas 中有两类非常重要的数据结构   即 Series（序列）和DataFrame(数据框)
# Series类似于numpy中的一维数组
# DataFrame类似于numpy中的二维数组

#series的创建
#通过一维数组创建序列
import numpy as np,pandas as pd

arr1 = np.arange(10)
print(arr1)
print(type(arr1))
# [0 1 2 3 4 5 6 7 8 9]
# <class 'numpy.ndarray'>

s1 = pd.Series(arr1)
print(s1)
print(type(s1))
# 0    0
# 1    1
# 2    2
# 3    3
# 4    4
# 5    5
# 6    6
# 7    7
# 8    8
# 9    9
# dtype: int32
# <class 'pandas.core.series.Series'>

#通过字典的方式创建序列
dic1 = {'a':10,'b':20,'c':30,'d':40,'e':50}
print(dic1)
print(type(dic1))
#
# {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# <class 'dict'>

#通过dataframe中的某一行或某一列创建序列

# DataFrame的创建

#通过二维数组创建数据框
arr2 = np.array(np.arange(12)).reshape(4,3)
print(arr2)
print(type(arr2))
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]
# <class 'numpy.ndarray'>
df1 = pd.DataFrame(arr2)
print(df1)
print(type(df1))
# 0   1   2
# 0  0   1   2
# 1  3   4   5
# 2  6   7   8
# 3  9  10  11
# <class 'pandas.core.frame.DataFrame'>

#通过字典的方式创建数据框
dic2 = {'a':[1,2,3,4],'b':[5,6,7,8],'c':[9,10,11,12],'d':[13,14,15,16]}
print(dic2)
print(type(dic2))
# {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12], 'd': [13, 14, 15, 16]}
# <class 'dict'>
df2 = pd.DataFrame(dic2)
print(df2)
print(type(df2))
#   a  b   c   d
# 0  1  5   9  13
# 1  2  6  10  14
# 2  3  7  11  15
# 3  4  8  12  16
# <class 'pandas.core.frame.DataFrame'>
dic3 = {'one':{'a':1,'b':2,'c':3,'d':4},'two':{'a':5,'b':6,'c':7,'d':8},'three':{'a':9,'b':10,'c':11,'d':12}}
print(dic3)
print(type(dic3))
df3 = pd.DataFrame(dic3)
print(df3)
print(type(df3))


#通过数据框的方式创建数据框
df4 = df3[['one','three']]
print(df4)
print(type(df4))

s3 = df3['one']
print(s3)
print(type(s3))
