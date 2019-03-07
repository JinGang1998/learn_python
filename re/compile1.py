# -*- coding: UTF-8 -*-
import re                     #[]   匹配内部的任一字符或子表达式    |逻辑或    .代表任意字符
pattern = re.compile(r'([a-z]+) ([a-z]+)',re.I) #re.I表示忽略大小写
m = pattern.match('Hello World Wide Web')
print(m)   #匹配成功，返回一个match对象
#<re.Match object; span=(0, 11), match='Hello World'>

print(m.group())   #返回匹配成功的整个子串
print(m.span())    #返回匹配成功的整个子串的索引
print(m.group(1))   #返回第一个分组匹配成功的子串
print(m.span(1))   #返回第一个分组匹配成功的子串的索引
print(m.group(2))  #返回第二个分组匹配成功的子串
print(m.span(2))   #返回第二个分组匹配成功的子串的索引
print(m.groups())   # 等价于 (m.group(1), m.group(2), ...)
print(m.group(3))   ## 不存在第三个分组
