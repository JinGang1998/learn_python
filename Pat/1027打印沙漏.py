a = input().split()   #获取输入  得到[个数，符号]
result = [a[1]]      #输出结果 初始化    起始为 1个输出 符号
n = int(a[0]) - 1      #n=个数-1
i = 3       #i 表示每行的 符号个数   以3  为首  等差数列   公差 为 2  递增
while n>0:
    #在列表 首  添加
    result.insert(0,i*a[1])     #insert()方法语法：                                list.insert(index, obj)                                参数                                    index -- 对象 obj 需要插入的索引位置。                                obj -- 要插入列表中的对象。'''
    #在列表尾  添加
    result.append(i*a[1])
    n -= 2*i   # n 递减
    i += 2     #i 递增
k = 0
#n 为 奇数
if n is 0:
    m = len(result[0])  #  第一行 的字符长度
    # 对齐
    for i in result:
        k += len(i)
        print("%s%s"%(" "*((m-len(i))//2),i))
#n  为偶数
else:
    m = len(result[1])
    for i in result[1:-1]:
        k += len(i)
        print("%s%s"%(" "*((m-len(i))//2),i))
print(int(a[0])-k)
