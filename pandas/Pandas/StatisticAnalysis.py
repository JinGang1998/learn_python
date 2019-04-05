import numpy as np
import pandas as pd
np.random.seed(1234)
d1 = pd.Series(2*np.random.normal(size=100)+3)
d2 = np.random.f(2,4,size=100)
d3 = np.random.randint(1,100,size=100)


print('非空元素计算：',d1.count())
print('最小值：',d1.min())
print('最大值：',d1,max())
print('最小值的位置: ',d1.idxmin())
print('最大值的位置: ', d1.idxmax()) #最大值的位置，类似于R中的which.max函数
print('10%分位数: ', d1.quantile(0.1)) #10%分位数
print('求和: ', d1.sum()) #求和
print('均值: ', d1.mean()) #均值
print('中位数: ', d1.median()) #中位数
print('众数: ', d1.mode()) #众数
print('方差: ', d1.var()) #方差
print('标准差: ', d1.std()) #标准差
print('平均绝对偏差: ', d1.mad()) #平均绝对偏差
print('偏度: ', d1.skew()) #偏度
print('峰度: ', d1.kurt()) #峰度
print('描述性统计指标: ', d1.describe()) #一次性输出多个描述性统计指标
# descirbe方法只能针对序列或数据框，一维数组是没有这个方法的

# 自定义一个函数，将这些统计描述指标全部汇总到一起
def stats(x):
    return pd.Series([x.count(),x.min(),x.idxmin(),x.quantile(.25),x.median(),x.quantile(.75),
                      x.mean(),x.max(),x.idxmax(),x.mad(),x.var(),x.std(),x.skew(),x.kurt()],
                     index = ['Count','Min','Whicn_Min','Q1','Median','Q3','Mean','Max',
                              'Which_Max','Mad','Var','Std','Skew','Kurt'])
print(stats(d1))


# 我们可能需要处理的是一系列的数值型数据框，如何将这个函数应用到数据框中的每一列呢？可以使用apply函数
# ，这个非常类似于R中的apply的应用方法。 将之前创建的d1,d2,d3数据构建数据框
df = pd.DataFrame(np.array([d1,d2,d3]).T,columns=['x1','x2','x3'])
print(df.head())
print(df.apply(stats))

# 非常完美，就这样很简单的创建了数值型数据的统计性描述。如果是离散型数据呢？就不能用这个统计口径了，我们需要统计
# 离散变量的观测数、唯一值个数、众数水平及个数。你只需要使用describe方法就可以实现这样的统计了

stu_dic = {'Age':[14,13,13,14,14,12,12,15,13,12,11,14,12,15,16,12,15,11,15],
'Height':[69,56.5,65.3,62.8,63.5,57.3,59.8,62.5,62.5,59,51.3,64.3,56.3,66.5,72,64.8,67,57.5,66.5],
'Name':['Alfred','Alice','Barbara','Carol','Henry','James','Jane','Janet','Jeffrey','John','Joyce','Judy','Louise','Marry','Philip','Robert','Ronald','Thomas','Willam'],
'Sex':['M','F','F','F','M','M','F','F','M','M','F','F','F','F','M','M','M','M','M'],
'Weight':[112.5,84,98,102.5,102.5,83,84.5,112.5,84,99.5,50.5,90,77,112,150,128,133,85,112]}
student = pd.DataFrame(stu_dic)
print(student['Sex'].describe())
# 除以上的简单描述性统计之外，还提供了连续变量的相关系数（corr）和协方
# 差矩阵（cov）的求解
print(df.corr())
# 关于相关系数的计算可以调用pearson方法或kendell方法或spearman方法，默认使用pearson方法
print(df.corr('spearman'))

# 如果只想关注某一个变量与其余变量的相关系数的话，可以使用corrwith,如下方只关心x1与其余变量的相关系数:
print(df.corrwith(df['x1']))

# 数值型变量间的协方差矩阵
print(df.cov())
