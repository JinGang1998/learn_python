import numpy as np
import matplotlib.pyplot as plt

# 通过subplot2grid实现
plt.figure()
# 通过栅格的形式创建布局方式,(3,3)创建3x3的布局形式，(0,0)绘制的位置，0行0列的位置绘制
# colspan:表示跨几列 rowspan:表示跨几行
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
# 在ax1图中绘制一条坐标(1,1)到坐标(2,2)的线段
ax1.plot([1, 2], [1, 2])
# 设置ax1的标题  现在xlim、ylim、xlabel、ylabel等所有属性现在只能通过set_属性名的方法设置
ax1.set_title('ax1_title')  # 设置小图的标题

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))
# 给对应的图绘制内容，这里只给ax4图绘制，属性通过set_xxx的模式设置
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')
plt.show()

# 通过gridspec实现
import numpy as np
import matplotlib.pyplot as plt
# 需要导入该模块
import matplotlib.gridspec as gridspec


plt.figure()
# 将整个视图分成3x3布局
gs = gridspec.GridSpec(3, 3)
# gs[0,:]  指定画图的位置 前面指定该图所占的行范围0表示0行，1: 表示从第一行到最后一行
# 第二个参数指定列的范围一个数表示固定列数，x:y表示从x列到y列
ax6 = plt.subplot(gs[0, :])
ax6.plot((0,1),(0,1))
# 第一行，从0列开始到2列，不包括2，也就是占0、1两列
ax7 = plt.subplot(gs[1, :2])
# 从第一行到最后，占1、2两行，后面的2表示只占用第二列，也就是最后的一列
ax8 = plt.subplot(gs[1:, 2])
# 倒数第一行，只占第0列这一列
ax9 = plt.subplot(gs[-1, 0])
# 倒数第一行，只占倒数第二列，由于总共三列，所以倒数第二列就是序号1的列
ax10 = plt.subplot(gs[-1, -2])
plt.show()


#通过subplots实现
import numpy as np
import matplotlib.pyplot as plt


# 这种方法只适合列数相同的布局
# sharex:所有小图共享x轴  sharey:表示所有小图共享y轴  坐标轴以所有小图中范围最大的进行显示
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1,2], [1,2])
ax12.plot((1,4),(1,4))
# 紧凑显示，边框会比较小，可以注释掉该行查看效果
plt.tight_layout()
plt.show()
