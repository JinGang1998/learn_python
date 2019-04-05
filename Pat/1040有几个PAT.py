'''in_list = [i for i in input()]
count = 0
for i in range(len(in_list)):
    if in_list[i]=='P':
        for j in range(i+1,len(in_list)):
            if in_list[j]=='A':
                for k in range(j+1,len(in_list)):
                    if in_list[k]=='T':
                        count += 1

count = count % 1000000007
print(count)'''           #存在超时

n = input()
count_P = count_PA = count_PAT = 0
for i in n:
    if 'P' == i:
        count_P += 1
    elif 'A' == i:
        count_PA += count_P
    else:
        count_PAT += count_PA
print(count_PAT % 1000000007)
