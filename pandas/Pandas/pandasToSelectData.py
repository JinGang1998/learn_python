import pandas as pd

stu_dic = {'Age':[14,13,13,14,14,12,12,15,13,12,11,14,12,15,16,12,15,11,15],
'Height':[69,56.5,65.3,62.8,63.5,57.3,59.8,62.5,62.5,59,51.3,64.3,56.3,66.5,72,64.8,67,57.5,66.5],
'Name':['Alfred','Alice','Barbara','Carol','Henry','James','Jane','Janet','Jeffrey','John','Joyce','Judy','Louise','Marry','Philip','Robert','Ronald','Thomas','Willam'],
'Sex':['M','F','F','F','M','M','F','F','M','M','F','F','F','F','M','M','M','M','M'],
'Weight':[112.5,84,98,102.5,102.5,83,84.5,112.5,84,99.5,50.5,90,77,112,150,128,133,85,112]}
student = pd.DataFrame(stu_dic)

#查询数据的前5行或末尾5行
# student.head()
# student.tail()
print(student.head())
#  Age  Height     Name Sex  Weight
# 0   14    69.0   Alfred   M   112.5
# 1   13    56.5    Alice   F    84.0
# 2   13    65.3  Barbara   F    98.0
# 3   14    62.8    Carol   F   102.5
# 4   14    63.5    Henry   M   102.5
print(student.tail())

#查询指定的行
# student.loc[[0,2,4,5,7]] #这里的loc索引标签函数必须是中括号[]
print(student.loc[[0,2,4,5,7]])

#查询指定的列
# student[['Name','Height','Weight']].head() #如果多个列的话，必须使用双重中括号
print(student[['Name','Height','Weight']].head())

#也可通过loc索引标签查询指定的列
# student.loc[:,['Name','Height','Weight']].head()
print(student.loc[:,['Name','Height','Weight']].head())

#查询出所有12岁以上的女生信息
print(student[(student['Sex']=='F')&(student['Age']>12)])

#查询出所有12岁以上的女生姓名、身高和体重
print(student[(student['Sex']=='F')&(student['Age']>12)][['Name','Height','Weight']])

# 如果是多个条件的查询，必须在&（且）或者|（或）的两端条件用括号括起来。
