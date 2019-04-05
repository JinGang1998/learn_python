import numpy as np
import pandas as pd
#增：添加新行或增加新列
stu_dic = {'Age':[14,13,13,14,14,12,12,15,13,12,11,14,12,15,16,12,15,11,15],
'Height':[69,56.5,65.3,62.8,63.5,57.3,59.8,62.5,62.5,59,51.3,64.3,56.3,66.5,72,64.8,67,57.5,66.5],
'Name':['Alfred','Alice','Barbara','Carol','Henry','James','Jane','Janet','Jeffrey','John','Joyce','Judy','Louise','Marry','Philip','Robert','Ronald','Thomas','Willam'],
'Sex':['M','F','F','F','M','M','F','F','M','M','F','F','F','F','M','M','M','M','M'],
'Weight':[112.5,84,98,102.5,102.5,83,84.5,112.5,84,99.5,50.5,90,77,112,150,128,133,85,112]}
student = pd.DataFrame(stu_dic)

# 在Excel中有一个非常强大的功能就是数据透视表，通过托拉拽的方式可以迅速的查看
# 数据的聚合情况，这里的聚合可以是计数、求和、均值、标准差等。 pandas为我们提供了非常强
# 大的函数pivot_table()，该函数就是实现数据透视表功能的。对于上面所说的一些聚合函数，可
# 以通过参数aggfunc设定。我们先看看这个函数的语法和参数吧：
#
# pivot_table(data,values=None,
#             index=None,
#             columns=None,
#             aggfunc='mean',
#             fill_value=None,
#             margins=False,
#             dropna=True,
#             margins_name='All')
# data：需要进行数据透视表操作的数据框
# values：指定需要聚合的字段
# index：指定某些原始变量作为行索引
# columns：指定哪些离散的分组变量
# aggfunc：指定相应的聚合函数
# fill_value：使用一个常数替代缺失值，默认不替换
# margins：是否进行行或列的汇总，默认不汇总
# dropna：默认所有观测为缺失的列
# margins_name：默认行汇总或列汇总的名称为'All'
Table1 = pd.pivot_table(student,values=['Height'],columns=['Sex'])
print(Table1)

# 对一个分组变量（Sex），两个数值变量（Height,Weight）作统计汇总
#
Table2 = pd.pivot_table(student,values=['Height','Weight'],columns=['Sex'])
print(Table2)

# 对两个分组变量（Sex，Age)，两个数值变量（Height,Weight）作统计汇总
Table3 = pd.pivot_table(student,values=['Height','Weight'],columns=['Sex','Age'])
print(Table3)

# 很显然这样的结果并不像Excel中预期的那样，该如何变成列联表的形式的？很简单，只需将
# 结果进行非堆叠操作（unstack）即可
Table4 = pd.pivot_table(student,values=['Height','Weight'],columns=['Sex','Age']).unstack()
print(Table4)

# 使用多个聚合函数
Table5 = pd.pivot_table(student,values=['Height','Weight'],columns=['Sex'],aggfunc=[np.mean,np.median,np.std])
print(Table5)
