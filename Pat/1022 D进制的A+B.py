def translate(a,x):
    m= a // x          #m 为商
    n= a % x        #n 为余数
    str1 = ''        #初始化
    while m!=0:            #
        str1 = str(n) + str1
        n = m % x
        m = m // x
    str1 = str(n) + str1
    return str1        #返回输出
a = input().split()
b = int(a[0])+int(a[1])
print(translate(b,int(a[2])))
