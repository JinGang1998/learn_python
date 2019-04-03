n = int(input())   #获取要输入 的人数
count = 0
max1 = ['','2014/09/06']  # the data of today
min1 = ['','1814/09/06']  #  没有超过这个年龄的人
for i in range(n):      #获取每个人的信息
    person = input().split()
    if '1814/09/06' <= person[1]<= '2014/09/06':   #person[1]     表示出生日期
        count += 1  #记录出生日期合理的 人数
        if person[1] < max1[1]:      #比较得到  年龄最大的人
            max1 = person
        if person[1] > min1[1]:      # 比较得到年龄最小的人
            min1 = person

if count == 0:
    print('0')
else:
    print(count,max1[0],min1[0])
