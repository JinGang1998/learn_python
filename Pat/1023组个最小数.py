#获取输入
n = input().split()
str1 = ''
for i in range(len(n)):   #字符串升序排序
    str1 += str(i)*int(n[i])
    #print(str1)
for i in range(len(str1)):  #找出第一个不为 0 的元素
    if str1[i]!='0':  #得到i
        break
print(str1[i],end="")  #输出第一个不为0的数
for j in range(0,i):     #
    print(str1[j],end="")
for j in range(i+1,len(str1)):
    print(str1[j],end="")
