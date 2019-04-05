num,s = input().split()
num = int(num)
print(num*s)#  第一行
if num%2!=0:                  #行数 为列数的1/2  四舍五入取整
    num1 = int(num/2)+1
else:
    num1 = int(num/2)
for i in range(num1-2): #行数 为列数 的1/2
    print(s+(num-2)*" "+s) #中间的行
print(num*s) #最后一行
