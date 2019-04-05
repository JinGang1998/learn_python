#输入要输入的个数
num = int(input())
dir = {}
max = '0'
dir[max] = 0

for i in range(num):
    my_num, value = input().split()               #编号 和 总分 分别 赋给  my_num  和  value
    value = int(value)               # 将其转为整型
    try:
        dir[my_num] += value
    except KeyError:              #集合键错误（不存在）时....
        dir[my_num] = value
    if dir[my_num] > dir[max]:         #比较得到最大
        max = my_num

print(max + ' '+str(dir[max]))  #标准输出

#有 超时  第5 个测试点
