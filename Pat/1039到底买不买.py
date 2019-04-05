h_give = [i for i in input()]        #所给 的球
m_need = [i for i in input()]         #我需要的球
#print(h_give)
count = 0
while count<len(m_need):
    if m_need[count] in h_give:            #如果 我需要的 在 所给 中
        h_give.remove(m_need[count])       #移除 对应的 两个 相同元素
        del m_need[count]
        count -= 1           #此时 列表 长度  -1
    count += 1       #递增  直至 遍历整个 列表
    # print(len(m_need))
if len(m_need)==0:          #如果 全部都在  所给 中
    print("%s %d"%("Yes",len(h_give)),end="")
else:
    print("%s %d"%("No",len(m_need)),end="")
