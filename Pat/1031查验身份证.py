x = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]  #权重分配
y = ['1','0','X','9','8','7','6','5','4','3','2']      #校验码M
n = int(input())       #输入的身份证  个数
m = 0                #用来判断 是否所有号码都正常
for i in range(n):
    num = str(input())      #获取 一个身份证 号码
    if len(num)>18:        #长度大于  18  则 打印 原身份证号
        print(num)
        m = 1
    else:
        a = num[:17]       #截取 前 17 位
        c = True
        b = 0
        for j in range(len(a)):#对前17为加权 求和
            try:                 # 测试 前 17位  是否全为 数字
                b += int(a[j])*x[j]
            except:
                c = False
                print(num)
                m = 1
                break
        if c:
            b = b%11   #求Z值
            if y[b]!=num[-1]:  #检查最后一位 校验码
                print(num)
                m = 1
if m==0:
    print('All passed')
