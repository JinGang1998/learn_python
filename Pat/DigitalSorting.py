
InputList = list(map(int,input().split()))  #输入
InputList = InputList[1:]     #第一个为测试用例，应将其出去
a1 = 0      #初始化 a1,a2,a3,a4,a5
a2 = 0
a3 = 0
a4 = 0
a5 = 0
count = 0   #计数 :满足a2条件的个数
List = []     #列表  存储满足a4数据
List1 = []     #列表1   存储满足a5数据

#for循环求 a1~a5
for i in InputList:
    if i%10==0:
        a1 += i
    elif i%5 == 1:
        count += 1
        if count%2 == 0:
            a2 = a2 - i
        else:
            a2 = a2 + i
    elif i%5 == 2:
        a3 += 1
    elif i%5 ==3:
        List.append(i)
    elif i%5 == 4:
        List1.append(i)

if len(List)>0:
    a4 = sum(List)/len(List)
    a4 = '%.1f'%(a4)
    print(a4)
else:
    a4 = 0
if len(List1)>0:

    a5 = max(List1)
else:
    a5 = 0
OutStr = [a1,a2,a3,a4,a5]
for i in range(0,5):
    if OutStr[i] == 0:
        OutStr[i] = 'N'

#此处应注意，a2为交错求和  ，当count>0时也有可能为0  此时对应输出N错误   故需加一个条件语句
if count > 0:
    OutStr[1] = a2
OutStr = list(map(str,OutStr))
print(' '.join(OutStr).strip())
#方法2
'''n=input().split()
m=int(n[0])
a=list(map(int,n[1:]))
A1,A2,A3,A4,A5=0,0,0,0,0#记录最终结果
k,j,flag=0,0,0#三个计算需要计数
for i in range(m):#循环判断和计算过程
    if a[i]%10==0:
        A1+=a[i]
    elif a[i]%5==1:
        flag=1
        A2+=a[i]*(-1)**k
        k+=1
    elif a[i]%5==2:
        A3+=1
    elif a[i]%5==3:
        A4+=a[i]
        j+=1
    elif a[i]%5==4:
        if a[i]>A5:
            A5=a[i]
#判断是否为空
if A1==0:
    A1="N"
if flag==0:
    A2="N"
if A3==0:
    A3="N"
if A4==0:
    A4="N"
else:
    A4='%.1f'%(A4/j)
if A5==0:
    A5="N"
print(A1,A2,A3,A4,A5)'''





