
#获取输入数字
n = input()

#print(int(n/100))
#求得输入数字的位数
num  = len(n)
#初始化UnitOut   后面用于表示个位数
UnitOut = ''
#当输入为三位数时
if num == 3:
    #得到个位数
    Theunit = int(n[2])
    #求得个位字符
    for i in range(1,Theunit+1):
        UnitOut = UnitOut + str(i)
    #得到输出字符
    OutStr = int(n[0])*'B'+int(n[1])*'S'+UnitOut
    # print(int(n[0])*'B',end='')
    # print(int(n[1])*'S',end='')
    #输出
    print(OutStr)
#输入为两位数
elif num == 2:
    Theunit = int(n[1])
    for i in range(1,Theunit+1):
        UnitOut = UnitOut + str(i)
    OutStr = int(n[0])*'S'+UnitOut
    print(OutStr)
#输入为一位数
elif num == 1:
    Theunit = int(n[0])
    for i in range(1,Theunit+1):
        UnitOut = UnitOut + str(i)
    OutStr = UnitOut
    print(OutStr)
#当超出三位判断错误
else:
    print("输入超出范围")

