#re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功返回none
#re.match(pattern,string,flags=0)   pattern:匹配的正则表达式
                                #  string:要匹配的字符串
                                #flags :控制匹配方式
                                     #re.I|M 多个匹配方式用|连接
                                     #re.I大小写不敏感
                                     #re.M多行匹配，影响^和$
                                     #re.S使匹配包括换行在内的所有字符
                                     #
#   匹配成功返回一个匹配的对象  ，否则返回none
# -*- coding: UTF-8 -*-
import re
print(re.match('www','www.python.org').span())   #在起始位置匹配
print(re.match('org','www.python.org'))   #在非起始位置匹配
#输出：
# (0, 3)
# None


line = "Cats are smarter than dogs"
# 首先，这是一个字符串，前面的一个 r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠，也就是忽略转义字符。但是这个字符串里没有反斜杠，所以这个 r 可有可无。
#
#  (.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
#  (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
#  后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
#我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式
if matchObj:
    print("matchObj.group() : ",matchObj.group())#group(num=0)num默认为0
    print("matchObj.group(1) : ",matchObj.group(1))
    print("matchObj.group(2) : ",matchObj.group(2))
else:
    print("No match!!!")
    #print("matchObj.group(3) : ",matchObj.group(3))
    # IndexError: no such group
# 输出：
# matchObj.group() :  Cats are smarter than dogs
# matchObj.group(1) :  Cats
# matchObj.group(2) :  smarter
