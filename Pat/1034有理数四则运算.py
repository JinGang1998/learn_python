def f(x):   #得到  有理数 的最简  形式
    a = x.split("/")   #得到 分子 与 分母
    if int(a[0]) == 0:            #判断  若 分子 为 0 则 为 0
        return "0"
    fz = int(a[0])//g(int(a[0]),int(a[1]))   #约分
    fm = int(a[1])//g(int(a[0]),int(a[1]))
    flag = 0
    if fz < 0: #判断正负
        flag = 1
    if abs(fz) >= fm:  #分子 绝对值  大于 分母
        if fz%fm == 0:      #判断 是否 整除
            if flag == 0:  #为正  正常 输出
                b = str(fz//fm)       #
            else:                #为  负  加括号
                b = "("+str(fz//fm)+")"
        else:#不整除
            if flag == 0:
                b = str(fz//fm)+" "+str(fz%fm)+"/"+str(fm)
            else:
                b = "(-"+str(fz*(-1)//fm)+" "+str(fz*(-1)%fm)+"/"+str(fm)+")"
    else:        #分子小于分母
        if flag == 0:
            b = str(fz)+"/"+str(fm)
        else:
            b = "("+str(fz)+"/"+str(fm)+")"
    return b

def g(i,j): #欧几里得算法 计算 公约数
    i = abs(i)  #求
    if i < j:  #交换 数值
        t = i
        i = j
        j = t
    d = i%j
    while d!=0:
        i=j
        j=d
        d=i%j
    return j

n = input().split()
a = n[0].split("/")   #将 第一个数 的 分子 分母  放入 列表 a  中
b = n[1].split("/")    # ... 第二个.........................b...
fz1 = int(a[0])   #分子1
fm1 = int(a[1])  # 分母1
fz2 = int(b[0])  # 分子2
fm2 = int(b[1])  # 分母2
res_jia = str(fz1*fm2+fz2*fm1)+"/"+str(fm1*fm2)  # 加法 的结果
res_jian = str(fz1*fm2-fz2*fm1)+"/"+str(fm1*fm2)    #减法
res_chen = str(fz1*fz2)+"/"+str(fm1*fm2)          #   乘法
if fz2 == 0:   #除法中  若  除数 为 0   则 输出 “Inf”
    res_chu="Inf"
else:
    res_chu=str(fz1*fm2)+"/"+str(fm1*fz2)         #除法
print("%s + %s = %s"%(f(n[0]),f(n[1]),f(res_jia)))
print("%s - %s = %s"%(f(n[0]),f(n[1]),f(res_jian)))
print("%s * %s = %s"%(f(n[0]),f(n[1]),f(res_chen)))
if fz2 != 0:
    print("%s / %s = %s"%(f(n[0]),f(n[1]),f(res_chu)))
else:
    print("%s / %s = %s"%(f(n[0]),f(n[1]),res_chu))
#  需要修改
