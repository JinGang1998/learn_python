num = input()           #学生人数
score = input().split()           #学生成绩
s_score = input().split()           #挑选 的分数个数  与分数
result = []            #空列表 用来方 结果
for i in s_score[1:]:       #遍历要挑选的分数，  并 在 score  中 搜索
    result.append(str(score.count(i)))
print(" ".join(result))     #输出


#有 超时 ...........
