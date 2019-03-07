# -*- coding: UTF-8 -*-
#re.search(pattern,string,flags=0) 扫描整个字符串并返回第一个成功的匹配。

import re
print(re.search('www','www.python.org').span()) #起始位置
print(re.search('org','www.python.org')) #非起始位置
# 输出：
# (0, 3)
# <re.Match object; span=(11, 14), match='org'>


line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*',line,re.M|re.I)

if searchObj:
    print("searchObj.group() : ",searchObj.group())
    print("searchObj.group(1) : ",searchObj.group(1))
    print("searchObj.group(2) : ",searchObj.group(2))
else:
    print("Nothing found!!!")
# 输出：
# searchObj.group() :  Cats are smarter than dogs
# searchObj.group(1) :  Cats
# searchObj.group(2) :  smarter
print(re.search('P','AAPAATAAAA').span())
print(re.search('A','AAPAATAAAA').span())
print(re.search('T','AAPAATAAAA').span())
