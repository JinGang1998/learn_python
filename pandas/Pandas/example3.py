'14.时间格式'
import time
import datetime
import pandas as pd
q = pd.datetime(2012,3,23)
p = pd.datetime.today()#datetime对象时间

#strftime  将对象时间转换成字符串时间
qstr = q.strftime("%Y-%m-%d %H:%M:%S")
ptup = pd.datetime.timetuple(p)  #转换成tumple时间

#striptime将字符串时间转换成tumple时间
qtup = time.strptime(qstr,"%Y-%m=%d %H:%M:%S")
qstamp = time.mktime(qtup)  #转换成时间戳
pstamp = time.mktime(ptup)

#计算两天的时间间隔
ndays = int((pstamp - qstamp)/(3600*24))
print(ndays)
