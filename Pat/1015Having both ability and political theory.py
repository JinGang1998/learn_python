def ranking(x):  #定义排序所用的条件以及判断顺序
    sum = -x[1]-x[2]  # 为了升序排列，故而取总分的负数作为参考key
    a = -x[1]  # 为了升序排列，故而取德分的负数作为第二参考key
    b = x[0]  # 学号作为第三参考key
    return sum,a,b  # 先总分，再德分，再学号
n, low, high = list(map(int, input().split()))  # 输入学生数、低分阈值和高分阈值
l1,l2,l3,l4,bad = [],[],[],[],0  # 将学生划为4类，l1到l4分别为一等生到四等生的列表，bad表示不及格人数
for row in range(n):
    i = list(map(int,input().split()))  # 获取每位学生的学号与成绩
    if i[1]<low or i[2]<low:  # 判断是否不及格
        bad += 1
    else:  # 对考生i按成绩划入相应列表
        if i[1]>=high:
            if i[2]>=high:
                l1.append(i)
            else:
                l2.append(i)
        else:
            if i[2]<=i[1]:
                l3.append(i)
            else:
                l4.append(i)
print(n-bad)  # 输出排序的学生数
for li in (l1,l2,l3,l4):  # 对每一类学生的列表进行内部排序并依次输出
    li = sorted(li, key=ranking)  # 对li中的学生按照ranking函数按题目指定的要求先总分，后德分再学号进行排序
    for stu in li:
        text = '{} {} {}'.format(*stu)
        print(text)
