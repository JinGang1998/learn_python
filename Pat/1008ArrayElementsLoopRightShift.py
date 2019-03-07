# m 为第一行输入
m = input().split()
n = input().split()
a = int(m[0])  #m[0]表示 要输入的数字个数
b = int(m[1])  #m[1]表示 要右移的位数
n1 = n[a-b:]
n2 = n[:a-b]
x = n1+n2
print(' '.join(x))

'''n = ['1','3','4','5','6','7']
n1 = n[4:]
n2 = n[:4]
x = n1 + n2
print(' '.join(x))'''
#当列表为字符时才可用join()
