# 一个是通过索引值或索引标签获取目标数据，另一个是通过索引，可以使序列或数据框的计算、操
# 作实现自动化对齐，下面我们就来看看这两个功能的应用
import numpy as np
import pandas as pd
#通过索引值或索引标签获取数据
s4 = pd.Series(np.array([1,1,2,3,5,8]))
print(s4)
# 如果不给序列一个指定的索引值，则序列自动生成一个从0开始的自增索引。
# 可以通过index查看序列的索引
print(s4.index)

s4.index = ['a','b','c','d','e','f']
print(s4)

# 序列有了索引，就可以通过索引值或索引标签进行数据的获取
print('s4[3]: ',s4[3])
print('s4[e]：',s4['e'])
print("s4[1,3,5]: ",s4[[1,3,5]])
print("s4[['a','b','d','f']]: ",s4[['a','b','d','f']])
print('s4[:4]: ',s4[:4])
print("s4['c':]：",s4['c':])
print("s4['b':'e']:",s4['b':'e'])

# 如果通过索引标签获取数据的话，末端标签所对应的值是可以返回的！在一维数组中，
# 就无法通过索引标签获取数据，这也是序列不同于一维数组的一个方面

#自动化对齐
s5 = pd.Series(np.array([10,15,20,30,55,80]),index=['a','b','c','d','e','f'])
print(s5)

s6 = pd.Series(np.array([12,11,13,15,14,16]),index=['a','c','g','b','d','f'])
print(s6)
print(s5+s6)
print(s5/s6)

# 由于s5中没有对应的g索引，s6中没有对应的e索引，所以数据的运算会产生两个缺失值NaN。注意，这里的算术结果就实现了两个序列索引的自动对齐，而非简单的将两个序列加总或相除。对于数据框的对齐，不仅仅是行索引的自动对齐，同时也会自动对齐列索引（变量名）
#
# 数据框中同样有索引，而且数据框是二维数组的推广，所以其不仅有行索引，而且还存在列索引，关于数据框中的索引相比于序列的应用要强大的多，这部分内容将放在数据查询中讲解。