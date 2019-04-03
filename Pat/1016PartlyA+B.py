Input_str = input().split()  #获取输入  并存入列表
str1 = ''  #初始化
str2 = ''
for i in Input_str[0]:
    if i == Input_str[1]:
        str1 += i
for i in Input_str[2]:
    if i == Input_str[3]:
        str2 += i
if str1=='':
    str1='0'
if str2=='':
    str2=='0'
print(int(str1)+int(str2))
