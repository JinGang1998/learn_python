'''P,A=input().split()  #获取 输入  P  and A
P = list(map(int,P.split('.')))     #将 P切割 为 列表
A = list(map(int,A.split('.')))      #同上
result = []       #创建 空列表 用于存储结果
def solve(P,A):
    if P[2]<=A[2]:        #计算 最后一位
        result.append(A[2]-P[2])
    else:
        result.append(A[2]+29-P[2])
        if A[1]>0:
            A[1]=A[1]-1
        else:
            A[0]=A[0]-1
            A[1]=9
    if P[1]<=A[1]:           #第二位
        result.insert(0,A[1]-P[1])
    else:
        result.insert(0,A[1]+17-P[1])
        if A[0]>0:
            A[0]=A[0]-1

    result.insert(0,A[0]-P[0])#  计算 第一位
    return result
# print(result)
if P[0]>A[0] or (P[0]==A[0] and P[1]>A[1]) or (P[0]==A[0] and P[1]==A[1] and P[2]>A[2]):
    result1 = solve(A,P)
    result1 = list(map(str,result1))
    print('-'+'.'.join(result1))
# result = list(map(str,result))
#print('.'.join(result))
else:
    result1 = solve(P,A)
    result1 = list(map(str,result1))
    print('.'.join(result1))'''                    #存在一个错误 点

# solution 2
P,A = input().split()
P = list(map(int,P.split('.')))
A = list(map(int,A.split('.')))
x = P[0]*17*29+P[1]*29+P[2]
y = A[0]*17*29+A[1]*29+A[2]
if x>y:
    max = x
    min = y
else:
    max = y
    min = x
result = max - min
result1 = result//29//17        #第一位
result -= result1*29*17
result2 = result//29            #第二位
result -= result2*29
result3 = result                 #第三位
if x>y:                              #P>A  P为 应付 A为 实际 付款   应付  大于 实付
    result1 = -result1
print("%d.%d.%d"%(result1,result2,result3))            #输出

