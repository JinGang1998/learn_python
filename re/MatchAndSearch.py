#-*- coding:UTF-8 -*-

import re
line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs',line,re.M|re.I)
if matchObj:
    print("match --> matchObj.group() : ",matchObj.group())
else:
    print("No match!!!")

SearchObj = re.search(r'dogs',line,re.M|re.I)
if SearchObj:
    print("search --> matchObj.group() : ",SearchObj.group())
else:
    print("No search!!!")

# 输出：
# No match!!!
# search --> matchObj.group() :  dogs
