# /*读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。
#
# 输入格式：
# 每个测试输入包含 1 个测试用例，即给出自然数 n 的值。这里保证 n 小于 10
# ​100
# ​​ 。
# 输出格式：
# 在一行内输出 n 的各位数字之和的每一位，拼音数字间有 1 空格，但一行中最后一个拼音数字后没有空格。*/
#输入正整数n并将其转为字符串
n=str(input())
#用m表示输入字符串的长度
m=len(n)
#初始化sum
sum=0
#遍历字符串n，将n的各位数字求和
for i in n:
    m=int(i,base=10)
    sum=sum+m
#将得到的和转为字符串形式
str1=str(sum)
#求长度
q=len(str1)
#提取sum的末尾数字
f=int(str1[q-1])

#for循环遍历sum第一位至倒数第二位的数字并输出相应拼音
for i in str1[:q-1]:
    s=int(i,base=10)
    if s==1:
        print('yi',end=" ")
    elif s==2:
        print('er',end=" ")
    elif s==3:
        print('san',end=" ")
    elif s==4:
        print('si',end=" ")
    elif s==5:
        print('wu',end=" ")
    elif s==6:
        print('liu',end=" ")
    elif s==7:
        print('qi',end=" ")
    elif s==8:
        print('ba',end=" ")
    elif s==9:
        print('jiu',end=" ")
    elif s==0:
        print('ling',end=" ")

#对sum的最后一位进行相应输出
if f==1:
    print('yi',end="")
elif f==2:
    print('er',end="")
elif f==3:
    print('san',end="")
elif f==4:
    print('si',end="")
elif f==5:
    print('wu',end="")
elif f==6:
    print('liu',end="")
elif f==7:
    print('qi',end="")
elif f==8:
    print('ba',end="")
elif f==9:
    print('jiu',end="")
elif f==0:
    print('ling',end="")
