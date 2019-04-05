from matplotlib import pyplot as plt
x = [5,2,7]
y = [2,16,4]
plt.plot(x,y)
plt.title('Image Title')
plt.ylabel('Y axis')
plt.xlabel('X axis')
#plt.show()

from matplotlib import style
style.use('ggplot')
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(x2,y2,'r',label='line two',linewidth=5)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()   #设置图例位置
plt.grid(True,color='k')
plt.show()
