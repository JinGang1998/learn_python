import re
#获得将要输入的字符串个数
InputTimes = int(input())

for i in range(1,InputTimes+1):
    #获取输入字符串，赋值给InputStr
    InputStr = input()

    #   *:匹配前一个字符0次或多次       +：匹配前一个字符一次或多次
    #[]   匹配内部的任一字符或子表达式    |逻辑或    .代表任意字符
    if re.match(r'A*PA+TA*',InputStr):
        a = re.split(r'[P|T]',InputStr)
        if a[0]*len(a[1])==a[2]:
            print("YES")
        else:
            print("NO")
    elif re.match(r'\s*PA+T\s*',InputStr):
        a = re.split(r'[P|T]',InputStr)
        if a[0]*len(a[1])==a[2]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")







