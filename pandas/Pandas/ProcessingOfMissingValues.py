# 现实生活中的数据是非常杂乱的，其中缺失值也是非常常见的，对于缺失值的存在可能会影响到后期的数据分析或挖掘工作，那么我们该如何处理这些缺失值呢？
# 常用的有三大类方法，即删除法、填补法和插值法。
#
#     删除法：当数据中的某个变量大部分值都是缺失值，可以考虑删除改变量；当缺失值是随机分布的，且缺失的数量并不是很多是，也可以删除这些缺失的观测。
#     替补法：对于连续型变量，如果变量的分布近似或就是正态分布的话，可以用均值替代那些缺失值；如果变量是有偏的，可以使用中位数来代替那些缺失值；对于离散型变量，我们一般用众数去替换那些存在缺失的观测。
#     插补法：插补法是基于蒙特卡洛模拟法，结合线性模型、广义线性模型、决策树等方法计算出来的预测值替换缺失值。
import numpy as np
import pandas as pd
#增：添加新行或增加新列
stu_dic = {'Age':[14,13,13,14,14,12,12,15,13,12,11,14,12,15,16,12,15,11,15],
'Height':[69,56.5,65.3,62.8,63.5,57.3,59.8,62.5,62.5,59,51.3,64.3,56.3,66.5,72,64.8,67,57.5,66.5],
'Name':['Alfred','Alice','Barbara','Carol','Henry','James','Jane','Janet','Jeffrey','John','Joyce','Judy','Louise','Marry','Philip','Robert','Ronald','Thomas','Willam'],
'Sex':['M','F','F','F','M','M','F','F','M','M','F','F','F','F','M','M','M','M','M'],
'Weight':[112.5,84,98,102.5,102.5,83,84.5,112.5,84,99.5,50.5,90,77,112,150,128,133,85,112]}
student = pd.DataFrame(stu_dic)
dic = {'Name':['LiuShunxiang','Zhangshan'],'Sex':['M','F'],'Age':[27,23],'Height':[165.7,167.2],'Weight':[61,63]}
student2 = pd.DataFrame(dic)
print(student2)
student3 = pd.concat([student,student2])
print(student3)

# 注意到了吗？在数据库中union必须要求两张表的列顺序一致，而这里concat函数可以自动对齐两个数据框的变量
#新增列
print(pd.DataFrame(student2,columns=['Age','Height','Name','Sex','Weight','Score']))
# 于新增的列没有赋值，就会出现空NaN的形式

#删: 删除表、观测行或变量列
del student2#删除数据框student2, 通过del命令可以删除python的所有对象
#print(student2)       NameError
#删除指定行
print(student.drop([0,1,3,6]))

# 根据布尔索引删除行数据，其实这个删除就是保留删除条件的反面数据，例如删除所有14岁以下的学生
print(student[student['Age']>14])

#删除指定列
print(student.drop(['Height','Weight'],axis=1).head())
# 我们发现，不论是删除行还是删除列，都可以通过drop方法实现，只需要设定好删除的轴即可，即调整drop方法中的axis参数。
# 默认该参数为0，表示删除行观测，如果需要删除列变量，则需设置为1。


#改：修改原始记录的值
student3.loc[student3['Name']=='LiuShunxiang','Height']=173
print(student3[student3['Name']=='LiuShunxiang'][['Name','Height']])



#查：有关数据查询部分，上面已介绍过了


#聚合：pandas模块中可以通过groupby()函数实现数据的聚合操作
# 根据性别分组，计算各组别中学生身高和体重的平均值
print(student.groupby('Sex').mean())

# 如果不对原始数据作限制的话，聚合函数会自动选择数值型数据进行聚合计算。如果不想对年龄计算平均值的话，就需要剔除改变量：
print(student.drop('Age',axis=1).groupby('Sex').mean())
# groupby还可以使用多个分组变量，例如根本年龄和性别分组，计算身高与体重的平均值
print(student.groupby(['Sex','Age']).mean())

# 还可以对每个分组计算多个统计量
print(student.drop('Age',axis=1).groupby('Sex').agg([np.mean(),np.median()]))


#排序
# 排序在日常的统计分析中还是比较常见的操作，我们可以使用sort_index和sort_values实现序列和数据框的排序工作
Data = pd.Series(np.array(np.random.randint(1,20,10)))
print(Data)
print(Data.sort_index())
print(Data.sort_values(ascending=False))

# 在数据框中一般都是按值排序
print(student.sort_values(by=['Age','Height']))



#多表连接
# 多表之间的连接也是非常常见的数据库操作，连接分内连接和外连接，在数据库语言
# 中通过join关键字实现，pandas我比较建议使用merger函数实现数据的各种连接操作。 如下是构造一张学生的成绩表
dic2 = {'Name':['Alfred','Alice','Barbara','Carol','Henry','Jeffrey','Judy','Philip','Robert','Willam'],
        'Score':[88,76,89,67,79,90,92,86,73,77]}
score = pd.DataFrame(dic2)

print(score)

# 现在想把学生表student与学生成绩表score做一个关联，该如何操作呢
stu_score1 = pd.merge(student,score,on='Name')
print(stu_score1)
# 默认情况下，merge函数实现的是两个表之间的内连接，即返回两张表中共同部分的数据。可以通过how参数设置连接的方式，
# left为左连接；right为右连接；outer为外连接

stu_score2 = pd.merge(student,score,on='Name',how='left')
print(stu_score2)
# 左连接实现的是保留student表中的所有信息，同时将score表的信息与之配对，能配多少配多少，
# 对于没有配对上的Name，将会显示成绩为NaN。
##*********************---------------------********************
s = stu_score2['Score']
print(s)

# 可以结合sum函数和isnull函数来检测数据中含有多少缺失值
print(sum(pd.isnull(s)))

#直接删除缺失值
print(s.dropna())

# 默认情况下，dropna会删除任何含有缺失值的行，我们再构造一个数据框试试
df = pd.DataFrame([[1,1,2],[3,5,np.nan],[13,21,34],[55,np.nan,10],[np.nan,np.nan,np.nan],[np.nan,1,2]],columns=('x1','x2','x3'))
print(df)
#
# 返回结果表明，数据中只要含有缺失值NaN,该数据行就会被删除，如果使用参数how=’all’，则表明只删除所有行为缺失值的观测;
#
# 使用一个常量来填补缺失值，可以使用fillna函数实现简单的填补工作：
#用0填补所有缺失值
print(df.fillna(0))
#采用前项填充或后项填充
print(df.fillna(method='ffill'))
print(df.fillna(method='bfill'))
#使用常量填充不同的列
print(df.fillna({'x1':1,'x2':2,'x3':3}))
x1_median = df['x1'].median()
x2_mean = df['x2'].mean()
x3_mean = df['x3'].mean()

print(x1_median)
print(x2_mean)
print(x3_mean)
print(df.fillna({'x1':x1_median,'x2':x2_mean,'x3':x3_mean}))
# 很显然，在使用填充法时，相对于常数填充或前项、后项填充，使用各列的众数、均值或中位数填充要更加合理一点，这也是工作中常用的一个快捷手段
