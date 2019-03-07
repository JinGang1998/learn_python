#re.compile(pattern[,flags]) 该函数用于编译正则表达式
#pattern: 一个字符串形式的正则表达式

import re
pattern = re.compile(r'\d+')  #用于匹配至少一个数字
m = pattern.match('one12twothree34four')   #查找头部，没有匹配
print(m)
#none
m = pattern.match('one12twothree34four',2,10) #从‘e’的位置开始匹配，没有匹配
print(m)
#none
m = pattern.match('one12twothree34four',3,10)#从‘1’的位置开始匹配，正好匹配返回一个match对象
print(m)
#<re.Match object; span=(3, 5), match='12'>
print(m.group())
#12

print(m.start())
#3
print(m.end())
#5
print(m.span())
#(3,5)
