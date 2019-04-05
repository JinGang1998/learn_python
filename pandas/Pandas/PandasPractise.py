import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#数据载入和总览

#数据载入
data = pd.read_csv(r'All.csv')

#数据合并
# pandas.concat可以沿着一条轴将多个对象堆叠到一起，这里我们要把data_01.csv/data_02.csv/data_03.csv三份数据集合并为一份数据进行后续分析处理
# pandas.concat可以沿着一条轴将多个对象堆叠到一起，这里我们要把data_01.csv/data_02.csv/data_03.csv三份数据集合并为一份数据进行后续分析处理
#查看前5行的数据
print(data.head())
#查看数据的信息，包括每个字段的名称、非空数量、字段的数据类型
print(data.info())

#用统计学指标快速描述数据的概要
print(data.describe())


#数据清洗

#缺失值处理
#从data.info()得知，contbr_employer、contbr_occupation均有少量缺失值,均填充为NOT PROVIDED
data['contbr_employer'].fillna('NOT PROVIDED',inplace=True)
data['contbr_occupation'].fillna('NOT PROVIDED',inplace=True)

#数据转换
# 利用字典映射进行转换：党派分析
#查看数据中总统候选人都有谁
print('共有{}候选人，分别是'.format(len(data['cand_nm'].unique())))
print(data['cand_nm'].unique())
#通过搜索引擎等途径，获取到每个总统候选人的所属党派，建立字典parties，候选人名字作为键，所属党派作为对应的值
parties = {
    'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican'
}

# 增加一列party存储党派信息
#通过map映射函数，增加一列party存储党派信息
data['party'] = data['cand_nm'].map(parties)
#查看两个党派的情况
print(data['party'].value_counts())

# 排序：按照职业汇总对赞助总金额进行排序

    #
    # DataFrame.sort_values(by, ascending=True, inplace=False)
    #
    # by是根据哪一列进行排序，可以传入多列；ascending=True是升序排序，False为降序；inplace=Ture则是修改原dataframe，默认为False
    #
data.groupby('contbr_occupation')['contb_receipt_amt'].sum().sort_values(ascending=False)[:20]
print(data)
# 利用函数进行数据转换：职业与雇主信息分析

#建立一个职业对应字典，把相同职业的不同表达映射为对应的职业，比如把C.E.O.映射为CEO
occupation_map = {
  'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
  'INFORMATION REQUESTED':'NOT PROVIDED',
  'SELF' : 'SELF-EMPLOYED',
  'SELF EMPLOYED' : 'SELF-EMPLOYED',
  'C.E.O.':'CEO',
  'LAWYER':'ATTORNEY',
}

# 如果不在字典中,返回x
f = lambda x: occupation_map.get(x, x)
data.contbr_occupation = data.contbr_occupation.map(f)

# 对雇主信息进行类似转换
emp_mapping = {
   'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
   'INFORMATION REQUESTED' : 'NOT PROVIDED',
   'SELF' : 'SELF-EMPLOYED',
   'SELF EMPLOYED' : 'SELF-EMPLOYED',
}

# If no mapping provided, return x
f = lambda x: emp_mapping.get(x, x)
data.contbr_employer = data.contbr_employer.map(f)



#数据筛选
# 赞助包括退款（负的出资额），为了简化分析过程，我们限定数据集只有正出资额
data = data[data['contb_receipt_amt']>0]

#候选人筛选
# 从下面可以卡出，赞助基本集中在Obama、Romney之间，为了更好的聚焦在两者间的竞争，我们选取这两位候选人的数据子集作进一步分析
#查看各候选人获得的赞助总金额
data.groupby('cand_nm')['contb_receipt_amt'].sum().sort_values(ascending=False)

#选取候选人为Obama、Romney的子集数据
data_vs = data[data['cand_nm'].isin(['Obama, Barack','Romney, Mitt'])].copy()


#面元化数据
# 利用cut函数根据出资额大小将数据离散化到多个面元中
bins = np.array([0,1,10,100,1000,10000,100000,1000000,10000000])
labels = pd.cut(data_vs['contb_receipt_amt'],bins)
print(labels)



#数据聚合与分组运算
# 分组计算Grouping，分组运算是一个“split-apply-combine”的过程：
#
#     拆分，pandas对象中的数据会根据你所提供的一个或多个键被拆分为多组
#     应用，将一个函数应用到各个分组并产生一个新值
#     合并，所有这些函数的执行结果会合并到最终的结果对象中

#透视表分析党派和职业
# 通过pivot_table根据党派和职业对数据进行聚合，然后过滤掉总出资不足200万美元的数据
#按照党派、职业对赞助金额进行汇总，类似excel中的透视表操作，聚合函数为sum
by_occupation = data.pivot_table('contb_receipt_amt',index='contbr_occupation',columns='party',aggfunc='sum')
#过滤掉赞助金额小于200W的数据
over_2mm = by_occupation[by_occupation.sum(1)>2000000]
print(over_2mm)
over_2mm.plot(kind='bar')
plt.show()


#分组级运算和转换
# 根据职业与雇主信息分组运算
# 我们接下来了解一下对Obama和Romney总出资最高的职业和雇主。注意，这里巧妙地利用了dict.get，它允许没有映射关系的职业也能“通过”
#由于职业和雇主的处理非常相似，我们定义函数get_top_amounts()对两个字段进行分析处理

def get_top_amounts(group,key,n=5):
#传入groupby分组后的对象，返回按照key字段汇总的排序前n的数据
    totals = group.groupby(key)['contb_receipt_amt'].sum()
    return totals.sort_values(ascending=False)[:n]

grouped = data_vs.groupby('cand_nm')
grouped.apply(get_top_amounts,'contbr_occupation',n=7)

# 从数据可以看出，Obama更受精英群体（律师、医生、咨询顾问）的欢迎，Romney则得到更多企业家或企业高管的支持
#同样的，使用get_top_amounts()对雇主进行分析处理
grouped.apply(get_top_amounts,'contbr_employer',n=10)


#对赞助金额进行分组分析(matplotlib画图)
# 统计各出资区间的赞助笔数，这里用到unstack()，stack()函数是堆叠，unstack()函数就是不要堆叠，即把多层索引变为表格数据
#labels是之前赞助金额离散化后的Series
grouped_bins = data_vs.groupby(['cand_nm',labels])
grouped_bins.size().unstack(0)
# 统计各区间的赞助金额
bucket_sums=grouped_bins['contb_receipt_amt'].sum().unstack(0)
print(bucket_sums)
#Obama、Romney各区间赞助总金额
bucket_sums.plot(kind='bar')
plt.show()

# 上图虽然能够大概看出Obama、Romney的赞助金额区间分布，但对比并不够突出，
# 如果用百分比堆积图效果会更好，下面我们就实现以下
#算出每个区间两位候选人收到赞助总金额的占比
normed_sums = bucket_sums.div(bucket_sums.sum(axis=1),axis=0)
print(normed_sums)
#使用柱状图，指定stacked=True进行堆叠，即可完成百分比堆积图
normed_sums[:-2].plot(kind='bar',stacked=True)
# 可以看出，小额赞助方面，Obama获得的数量和金额比Romney多得多

# 按照赞助人姓名分组计数，计算重复赞助次数最多的前20人
data.groupby('contbr_nm')['contbr_nm'].count().sort_values(ascending=False)[:20]



#时间处理

# str转datetime
# 我们可以使用to_datetime方法解析多种不同的日期表示形式。对标准日期格式（如ISO8601）的解析非常快
# 。我们也可以指定特定的日期解析格式，如pd.to_datetime(series,format='%Y%m%d')
data_vs['time'] = pd.to_datetime(data_vs['contb_receipt_dt'])

# 以时间作为索引
data_vs.set_index('time',inplace=True)
data_vs.head()


# 重采样和频度转换
# 重采样（Resampling）指的是把时间序列的频度变为另一个频度的过程。把高频度的数据变为低频度叫做降采样（downsampling），
# resample会对数据进行分组，然后再调用聚合函数。这里我们把频率从每日转换为每月，属于
# 高频转低频的降采样。
vs_time = data_vs.groupby('cand_nm').resample('M')['cand_nm'].count()
vs_time.unstack(0)

# 我们用面积图把11年4月-12年4月两位总统候选人接受的赞助笔数做个对比
# 可以看出，越临近竞选，大家赞助的热情越高涨，奥巴马在各个时段都占据绝对的优势
fig1, ax1=plt.subplots(figsize=(32,8))
vs_time.unstack(0).plot(kind='area',ax=ax1,alpha=0.6)
plt.show()
