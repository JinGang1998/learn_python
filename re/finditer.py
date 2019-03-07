#和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
#re.finditer(pattern,string,flags=0)

# -*- coding: UTF-8 -*-

import re

it = re.finditer(r"\d+","12a32bc43gh3")
for match in it:
    print(match.group())

# 输出：
#
# 12
# 32
# 43
# 3
