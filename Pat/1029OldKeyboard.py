a = input()     #应该输入的文字
b = input()        #实际输入的文字
x = []
y = []
for i in a:  #将 应该输入的 字符  添加到 x 中
    x.append(i)
for i in b:       #去除 a  中所含有 的 b中的元素
    x.remove(i)
for i in range(len(x)):
    #将 小写字母 转换为  大写
    if ord(x[i])>=ord('a') and ord(x[i])<=ord('z'):
        x[i] = chr(ord(x[i])-ord('a')+ord('A'))   # 将 小写字符 转换为 大写
result = []
for i in x:
    if i not in result:
        result.append(i)
for i in result:
    print(i,end="")
