# dict2 = {}
# dict2[3] = 'sssfw'
# dict2[1] = 'wqrqwtqg'
# print(dict2)
# 输出：
# {3: 'sssfw', 1: 'wqrqwtqg'}



#获取学生个数
InputNumber = int(input())
#创建字典用于存储学生信息  用学生的分数作为键（key）
dict1 = {}
#创建列表用于存储学生的分数
StudentList = []

for i in range(InputNumber):
    #获取输入的学生信息并赋给a
    a = input().split()
    #
    dict1[int(a[2])]=a[0] + ' '+a[1]
for key in dict1:
    StudentList.append(key)
print(dict1[max(StudentList)])    #max(List)  获取列表中的最大值
print(dict1[min(StudentList)])


    #name,StudentNum,Score = input().split()
    #Studentdict = {'Name':name,'StudentNum':StudentNum,'Scores':Score}
    #StudentList.append(Studentdict)



