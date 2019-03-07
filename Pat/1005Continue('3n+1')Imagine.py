#得到输入数字个数
n = int(input())
#将输入分割成列表
num_list = input().split()

Listed = set()   #所有遍历过的数字集合
res = []        #关键数列表


for num in num_list:
    num = int(num)
    #当遍历过的数字集合中没有，则将该数字加入res中
    if num not in Listed:
        res.append(num)

        r = num

        #遍历数字加入Listed中
        while r!=1 and r not in Listed:
            Listed.add(int(r))
            if r % 2 == 0:
                r = r/2
            else:
                r = (3*r+1)/2

        if r in res:
            res.remove(r)

#列表排序
res.sort(reverse=1)

#输出
for num in res:
    #最后一个字符输出结束为空字符
    if num == res[-1]:
        print(num)
        break
    print(num,end=' ')   #前面的字符以空格结尾


# m = set()
# m.add(4)
# m.add(45)
# print(m)
#输出
# {4, 45}
