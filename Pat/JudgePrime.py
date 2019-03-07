import time
import math
#根据素数定义
def prime(n):
    if n<=1:
        return False
    #for循环判断是否为合数，若为合数返回false
    for i in range(2,n-1):
        if n%i==0:
            return False

    return True
#print(prime(4))

#优化1：实际只需计算2—\sqrt{n}  即可，经过这步优化计算量变为1/2
def prime1(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i ==0:
            return False
    return True

#除了2（2是素数）以外的其他偶数都不是素数，除了3（3是素数）以外其他能被3整除的数都不是素数，所以我们每找到一个素数，那么它的整数倍都不是素数。
def prime2(n):
    flag = [1]*(n+2)
    p=2
    while(p<=n):
        print(p)
        for i in range(2*p,n+1,p):
            flag[i] = 0
        while 1:
            p += 1
            if(flag[p]==1):
                break

print(prime2(10))


