'''k,d = map(int,input().split())
S_list = list(map(int,input().split()))
TP_list = list(map(int,input().split()))
P_list = []
for i in range(0,k):
    #P_list.append('%.2f'%(TP_list[i]/S_list[i]))
    P_list.append(TP_list[i]/S_list[i])
P_list = list(map(float,P_list))

#x = P_list.index(max(P_list))
print(P_list)
sum = 0
while True:
    x = P_list.index(max(P_list))
    #print('x',x)
    if d>=S_list[x]:

        sum = sum + P_list[x]*S_list[x]
        #print(sum)
        d = d-S_list[x]
        S_list[x]=0
        P_list[x]=0
    elif d>0 and d<S_list[x]:
        sum = sum + P_list[x]*d
        #print(sum)
        d = 0
    if d == 0:
        sum = '%.2f'%sum
        print(sum)
        break'''      #自己写的       第四点超时  还有一点  非零返回

n, space = list(map(int, input().split()))
size = list(map(float, input().split()))
price = list(map(float, input().split()))
rate = {i: price[i]/size[i] for i in range(n)}
order = sorted(rate, key=lambda i:rate[i], reverse=True)
money = 0
for i in order:
    if space >= size[i]:
        money += price[i]
        space -= size[i]
    else:
        money += space * rate[i]
        break
print('%.2f' % money)

