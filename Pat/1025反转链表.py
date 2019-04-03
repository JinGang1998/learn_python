a = input().split()     #获取第一行输入
b = []
for i in range(int(a[1])):     #a[1]   表示输入的链表的个数
    b.append(input().split())        #将每个链表输入都存储在  b[]  中
x = []
for i in b:
    if i[0]==a[0]:     #将顺序第一的链表 放入x  中
        x.append(i)
while x[-1][2]!='-1':   # 当 NEXT 不为 -1  时  顺序添加  到 x    x 为顺序排列的  链表
    for i in b:
        if i[0]==x[-1][2]:
            x.append(i)
m = []
i = 0
while i<int(a[1]):
    m.append(x[i:i+int(a[2])])        #a[2]   表示需要翻转的 元素个数
    i+=int(a[2])          #将需要翻转的元素 加入 m 中    列表切片  x中  只有 6个元素   x[4:8]  返回   第5和 6  个元素
# m=[[['00100', '1', '12309'], ['12309', '2', '33218'], ['33218', '3', '00000'], ['00000', '4', '99999']], [['99999', '5', '68237'], ['68237', '6', '-1']]]
for i in m:
    if len(i)<int(a[2]):  #个数小于a[2]  则打断
        break
    else:
        i.reverse()           #翻转
        j=0
        while j<int(a[2])-1:       #将 链表 的位置更正
            i[j][2]=i[j+1][0]
            j+=1
for i in range(len(m)-1):
    m[i][-1][2]=m[i+1][0][0]
if len(m[-1])==int(a[2]):
    m[-1][int(a[2])-1][2]='-1'
##  输出结果
for i in m:
    for j in i:
        print("%s %s %s"%(j[0],j[1],j[2]))
