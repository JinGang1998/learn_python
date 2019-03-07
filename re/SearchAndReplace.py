# -*- coding: UTF-8 -*-

#re.sub(pattern,repl,string,count=0,flags=0)
# pattern:正则中的模式字符串
# repl:替换的字符串，也可以为一个函数
# string:要被查找替换的原始字符串
# count: 模式匹配后替换的最大次数，默认为0表示替换所有的匹配

import re
phone = "2019-991-666 # 这是一个国外电话号码"

#repl不是函数


#删除字符串中的Python 注释
num = re.sub(r'#.*$',"",phone)
print("电话号码是：",num)

#删除非数字（-）的字符串
num = re.sub(r'\D',"",phone)
print("电话号码是：",num)

# 输出：
# 电话号码是： 2019-991-666
# 电话号码是： 2019991666

#repl是一个函数


def double(matched):
    value = int(matched.group('value'))
    return str(value*2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)',double,s))
# 输出：
# A46G8HFD1134
