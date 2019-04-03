#有N根绳子，第i根绳子的长度为Li,现在需要M根等长的绳子，你可以对n根绳子进行任意裁剪，（不能拼接），请你帮忙计算出
# 这m根绳子最长的长度是多少
list1 = list(map(int,input().split()))   #获取第一行输入  N和M  N根原始的绳子，最终需要的M根绳子数
list2 = list(map(int,input().split()))  #第二行输入包含N个整数   第i个整数Li表示第i根绳子长度
n = list1[0] #获取N
m = list1[1]  #获取M
x = max(list2)   #设置绳子长度初始值
while True:
    num = 0  #初始化 num用于表示以当前长度可得到的绳子数
    for i in list2:
        #print('x=',x)
        num += int(i/x)
        #print('num= ',num)
    #print(x)

    if num == m:
        print('%.2f'%x)
        break
    else:
        x = x-0.01
        x = '%.2f'%x       #设置为两位小数  不然随次数增加会出现误差
        x = float(x)      #由str转为浮点型
