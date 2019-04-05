'13.常用统计函数'
import pandas as pd
import numpy as np
dates = pd.date_range('20170501',periods=6)
df = pd.DataFrame(data=np.random.randn(6,5),index=dates,columns=list('ABCDE'))
a = df.describe()
print(a)
dfchange = df.pct_change()  #求每日变化比例
print(dfchange.fillna(0))

'''
count  非NA值的数量
describe  针对 Series 或 DF 的列计算汇总统计
min,max        最小值和最大值
idxmin  , idxmax   最小值和最大值的索引值
quantile         样本分位数（0到1）
sum             求和
mean             均值
median            中位数
mad                根据均值计算平均绝对利差
var               方差
std               标准差
skew               样本的偏度(三阶矩)
kurt                样本的峰度（四阶矩）
cumsum              样本的累计和
cummin , cummax        样本的累积和最大值和累积和最小值
cumprod               样本值的累计积
diff                  计算一阶差分
pct_change             计算百分数变化
'''

'14.时间格式'
