a = input().split()  #获取输入  切割为 列表
b = (int(a[1])-int(a[0]))/100  # b  表示秒数
h = int(b//3600)         #  h -> 小时数
b = b - h*3600         #   总秒数 -  小时 所占 秒数
m = int(b//60)   #  得到  分钟数
b = b - m*60      #得到剩余  s 数
s = b        #秒数
if '.' in str(s):   #实现 秒数的 四舍五入
    x = str(s).split('.')
    y = '0.'+x[1]
    if float(y)>=0.5:
        s = int(x[0])+1
    else:
        s = int(x[0])

if h<10:            # 小时数 <10    在 数字前 加0  对齐
    h = '0'+str(int(h))
if m<10:            #同上
    m = '0'+str(int(m))
if int(s)<10:               #同上
    s = '0'+str(int(s))
print("%s:%s:%s"%(h,m,str(s)))        #输出
