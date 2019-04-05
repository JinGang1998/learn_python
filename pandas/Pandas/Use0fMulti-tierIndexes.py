# 最后我们再来讲讲pandas中的一个重要功能，那就是多层索引。在序列中它可以实
# 现在一个轴上拥有多个索引，就类似于Excel中常见的这种形式
import numpy as np
import pandas as pd
# Series的层次化索引，索引是一个二维数组，相当于两个索引决定一个值
# 有点类似于DataFrame的行索引和列索引
s = pd.Series(np.arange(1,10),index=[["a","a","a","b","b","c","c","d","d"],[1,2,3,1,2,3,1,2,3]])
print(s)
print(s.index)

#选取外层索引为a的数据
print(s['a'])
#选取外层索引为a和内层索引为1的数据
print(s['a',1])
#选取外层索引为a和内层索引为1,3的数据
print(s['a'][[1,3]])
#层次化索引的切片，包括右端的索引
print(s[['a','c']])
print(s['b':'d'])
#通过unstack方法可以将Series变成一个DataFrame
#数据的类型以及数据的输出结构都变成了DataFrame，对于不存在的位置使用NaN填充
print(s.unstack())

#DataFrame的层次化索引
data = pd.DataFrame(np.random.randint(0,150,size=(8,12)),
                    columns = pd.MultiIndex.from_product([['模拟考','正式考'],
                                                   ['数学','语文','英语','物理','化学','生物']]),
               index = pd.MultiIndex.from_product([['期中','期末'],
                                                   ['雷军','李斌'],
                                                  ['测试一','测试二']]))
print(data)
print(data['模拟考'][['语文','数学']])
print(data.loc['期中','雷军','测试一']['模拟考','数学'])
print(data.loc['期中','雷军','测试一'])
print(data.iloc[0])
print(data['正式考'])
