input_list = list(map(int,input().split()))
m = input_list[0]
n = input_list[1]
def prime(n,result):
    flag = [1]*(n+2)
    p=2
    while(p<=n):
        result.append(p)
        for i in range(2*p,n+1,p):
            flag[i] = 0
        while 1:
            p += 1
            if(flag[p]==1):
                break

result = []
prime(200000,result)
final = result[m-1:n]
out_list = list(map(str,final))
if len(out_list)<=10:
    print(' '.join(out_list))
else:
    for i in range(0,int(len(out_list)/10)):
        print(' '.join(out_list[i*10:(i+1)*10]))
    print(' '.join(out_list[int(len(out_list)/10)*10:len(out_list)]))
