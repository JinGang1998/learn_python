n = int(input())
OutStrList = []
for i in range(0,n):
    s = list(map(int,input().split()))
    #print(s)
    if s[0]+s[1]>s[2]:
        OutStrList.append('Case #'+str(i+1)+': true')
        #print('Case #'+str(i+1)+': false')
    else:
        OutStrList.append('Case #'+str(i+1)+': false')
        #print('Case #'+str(i+1)+': true')

for i in OutStrList:
    print(i)

