#输入数字
a = input()
# i 表示数字   a.count(str(i))  用来统计 i 出现的次数
for i in range(10):
    if a.count(str(i))!=0:
        print("%d:%d"%(i,a.count(str(i))))   #输出   %d 表示整型数据
