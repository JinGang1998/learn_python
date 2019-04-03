#map(function, iterable, ...)    iterable   一个或多个序列
x = list(map(int,input().split()))
n = len(x)

#print(xorder)
OutList = []
for i in range(0,n,2):
    coefficient = x[i]
    index = x[i+1]
    if index == 0:
        continue
    OutList.append(str(coefficient*index))
    OutList.append(str(index-1))
outStr = ' '.join(OutList)
#print(outStr)
if outStr:
    print(outStr.strip())    #str.strip([chars]);   移除头尾的字符
else:
    print('0 0')
