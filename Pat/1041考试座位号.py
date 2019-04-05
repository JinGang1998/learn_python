num = int(input())  #学生个数
stu_mes = []        #存储学生信息
for i in range(num):         #信息添加
    stu_mes.append(input().split())
M = input()             #要查询 的 数量
sj_num = input().split()      #试机座位
for i in sj_num:
    for j in stu_mes:
        if i==j[1]:
            print("%s %s"%(j[0],j[2]))
