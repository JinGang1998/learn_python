n,p = [int(i) for i in input().split()]  #获取 n  和 p
b = sorted(list(map(int,input().split())))       # 得到b  将这些数  有小到大 排序 放在 列表中
m = 0        #表示 最美数列长度   此处为 初始化
for i in range(n):
    #i  为 起始位置
    next_ = i+m    #完美数列最大项 +1,  作为内层完美数列最大项循环的下界
    if next_ >= n:
        break
    for j in range(next_,n):
        # j  为  终止位置
        if b[i]*p<b[j]:  # 当最小值与p  的乘积小于最大值   则  结束循环
            break
        m += 1
print(m)
