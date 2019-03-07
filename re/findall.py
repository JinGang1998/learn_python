# -*- coding:UTF8 -*-
#在字符串中找到正则表达式所匹配的所有子串
#match 和 search 是匹配一次 findall 匹配所有
#findall(string[,pos[,endpos]])
#pos 指定字符串的起始位置
#endpos 指定字符串的结束位置

import re

pattern = re.compile(r'\d+')  #查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456',0,10)

print(result1)
print(result2)
# 输出：
# ['123', '456']
# ['88', '12']
