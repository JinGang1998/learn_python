#可以认为该题  在一个字符串中按要求移动小数点 ，并适当添加 0
a = input().split('E')
b = a[0][0]    #b 表示 正负
a[0] = a[0][1:len(a[0])]   #a[0]   表示有效数字的绝对值
str1 = ""
# 定位小数点位置
if '.' in a[0]:
    x = a[0].index('.')   #  x  表示 小数点位置
    str1 = str1 + a[0][0:x]+a[0][x+1:len(a[0])]  #得到 除去 小数点后的数

else:

    print("输入格式有误！")
    #str1 = a[0]
if int(a[1])<0:  #小数点超出范围，添加字符'0'
    x = x+int(a[1])
    if x<=0:
        str1 = '0'+'.'+(-x)*'0'+str1
    elif x>0:
        str1 = str1[0:x]+'.'+str1[x:len(str1)]
elif int(a[1])>0:
    x = x + int(a[1])
    if x>len(str1):
        str1 = str1+'0'*(x-len(str1))
    elif x<len(str1):
        str1 = str1[0:x]+'.'+str1[x:len(str1)]
elif int(a[1])==0:
    str1=a[0]

if b=='-':
    str1='-'+str1
print(str1)
