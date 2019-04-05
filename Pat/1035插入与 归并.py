def Insertsort(n,m):#插入排序是迭代算法，逐一获得输入数据，逐步产生有序的输出序列。每步迭代中，算法从输入序列中取出一元素，将之插入有序序列中正确的位置。如此迭代直到全部元素有序。
    x = 0
    for i in range(1,len(n)):
        k = n[:i+1]   #截取部分
        k.sort()           #部分排序
        k.extend(n[i+1:])   #extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
        if x==1:
            return k
        if k==m:      #若与中间 序列 相等 则 再 迭代 一次 ， 并 返回 迭代 一次后的结果
            x = 1
    return False      #若 始终 与中间 序列 不相等  则 返回 False

def Mergesort(n,m):#归并排序进行如下迭代操作：首先将原始序列看成 N 个只包含 1 个元素的有序子序列，然后每次迭代归并两个相邻的有序子序列，直到最后只剩下 1 个有序的序列。
    x = 0
    n = [[i] for i in n]  #将原是序列 分为 N个 只包含一个元素的有序子列
    while len(n)>1:
        k = []
        for j in range(0,len(n),2):#将 n 中 序列 两个 两个的填到 k 中     ->  归并
            try:
                n[j].extend(n[j+1])
                k.append(n[j])
            except:
                k.append(n[j])
        for i in k:  #排序
            i = i.sort()
        n = k[:]  #将排序 好  的 列表组 重新 赋给 n
                                            #         print("###########",n)
                                            #         1 3 2 8 5 7 4 9 0 6
                                            # ########### [[1, 3], [2, 8], [5, 7], [4, 9], [0, 6]]
                                            # ########### [[1, 2, 3, 8], [4, 5, 7, 9], [0, 6]]
                                            # Merge Sort
                                            # 1 2 3 8 4 5 7 9 0 6
        result = []
        for i in k:#将 二维 列表 重新 变为 1维
            for l in i:
                result.append(l)
        if x==1:  #在迭代 一次 返回 结果
            return result
        if result==m:   #若 中间 序列 与其相等 则 再 迭代 一次
            x = 1

n = input()          #序列长度
a = [int(i) for i in input().split()]  #原始序列
b = [int(i) for i in input().split()]  #中间序列
a1 = a[:]             #a1  用于 存储 a
m = Insertsort(a,b)     #对 a,b 进行  插入排序， 将 返回值 赋给 m
if m!=False:           #未返回 FALSE      则为  插入排序  输出中间序列 再 迭代一次 的结果
    print("Insertion Sort")
    for i in range(len(m)-1):
        print(m[i],end=" ")
    print(m[i+1],end="")
else:              #否则  为 归并排序
    m = Mergesort(a1,b)
    print("Merge Sort")
    for i in range(len(m)-1):
        print(m[i],end=" ")
    print(m[i+1],end="")
