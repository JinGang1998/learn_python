'''
pandas 中常用的数据结构有：
（1）Series：一维数组，与Numpy中的一维array类似。
Series中只允许存储相同的数据类型。
（2）DataFrame：二维的表格型数据结构。
可以将DataFrame理解为Series的容器。
（3）Panel ：三维的数组，可以理解为DataFrame的容器。
'''
'1.Series对象'
import numpy as np
import pandas as pd
s = pd.Series([1,np.nan,6,8])
s.index = ['one','two','three','four']
print(s)
print(s.index)

'2.创建dataframe对象'
dates = pd.date_range('20130101',periods=3)
df = pd.DataFrame(np.random.randn(3,4),index=dates,columns=list('ABCD'))
print(df)

'3.从excel中读入DataFrame对象'
classmates = pd.read_excel('classmates.xlsx')
classmates.columns = ['name','age','gender']
print(classmates)

'4.增加行'
classmates.loc[3] = {'name':'安妮','age':'24','gender':'女'}
classmates = classmates.append(pd.DataFrame([['丽丽','女','32']],\
                                            columns=classmates.columns),ignore_index=True)
#ignore_index = True 表示重置索引
print(classmates)

'5.删除行'
#drop 和 append 作用相反
classmates = classmates.drop([3]) #删除并生成新的数据框
print(classmates)

'6.增加列'
hobby = ['浪','耍','约']
classmates['hobby'] = hobby
height = [170,160,165]
classmates.insert(2,'height',height) #插入到第三列
print(classmates)

'7.删除列'
classmates = classmates.drop(['height'],axis = 1)
del classmates['hobby']  #永久删除
print(classmates)

'8.移动列'
#将gender 移动到 age前面
gender = classmates.pop('gender')#先弹出
classmates.insert(1,'gender',gender)  #再插入到适当的位置
print(classmates)

'9.排序'
a1 = classmates.sort_values(['name','age'],ascending=[0,1])  #按列排序
a = classmates.sort_index()  #按索引排序
print(a1)

'10.拼接'
friends = pd.DataFrame([['李雷','浪'],['大锤','约']],columns=['name','hobby'],index=['LiLei','Dachui'])
classmates.index = ['LiLei','HanMeiMei','Ann']
friends = friends.drop(['name'],axis= 1)

#使用concat 函数拼接，纵向拼接
oldguys = classmates.join(friends,how = 'inner')
print(oldguys)

'11.选取数据'
print(classmates.shape)   #查看形状
print(classmates.head(3))   #前3行
print(classmates.tail(3))   #后3行
print(classmates[1:3]) #选择多行
print(classmates['LiLei':'Ann'])  #选择多行
print(classmates.name)  #提取一列返回series
print(classmates[['name','age']]) #选择多列
print(classmates.loc['LieLei':'Ann',:])  #用标签查看数据
#classmates.iloc[0:2,:]  #用下标查看数据


#布尔索引
#classmates[(classmates['age']>22)&(classmates.age<24)]

'12.导出csv文件或excel文件'
classmates.to_csv('myclassmates.csv')
#使用writer 可以在一个excel 文档里写多个表格

#导出dataframe 到指定sheet
classmates.to_excel('myclassmates.xlsx','sheet2')

#导出多个dataframe到同一个excel 表格多个sheet
friends = classmates[0:1].copy()
writer = pd.ExcelWriter("oldguys.xlsx")
classmates.to_excel(writer,sheet_name="classmates")
friends.to_excel(writer,sheet_name="friends")
writer.save()
