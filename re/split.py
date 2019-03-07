#split 方法按照能够匹配的子串将字符串分割后返回列表
#re.split(pattern,string[,maxsplit=0,flags=0])
#maxsplit :分隔次数  默认为0
import re

result1 = re.split('\W+','runoob,runoob,runoob.')
print(result1)

result2 = re.split('(\W+)','runoob,runoob,runoob.')
print(result2)

result3 = re.split('\W+','runoob,runoob,runoob.',1)  #\W+   其中\W表示匹配非字母数字下划线
print(result3)                                            #  +表示匹配前一个字符或子表达式一次或多次
#对于找不到匹配的字符串而言，split不会对齐分割
result4 = re.split('a*','hello world')
print(result4)

print(re.split(r'[P|T]','PAT'))
print(re.split(r'[P|T]','AAAPATAA'))
