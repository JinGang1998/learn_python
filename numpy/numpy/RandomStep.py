# 我们通过模拟随机漫步来说明如何运用数组运算。先来看一个简单的随机
# 漫步的例子：从0开始，步长1和－1出现的概率相等。
import random
import matplotlib.pyplot as plt
import numpy as np
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

plt.plot(walk[:100])

# 不难看出，这其实就是随机漫步中各步的累计和，可以用一个数组运算来实现。因此，
# 我用np.random模块一次性随机产生1000个“掷硬币”结果（即两个数中任选一个），
# 将其分别设置为1或－1，然后计算累计和
nsteps = 1000
draws = np.random.randint(0,2,size=nsteps)
steps = np.where(draws > 0,1,-1)
walk = steps.cumsum()
# 有了这些数据之后，我们就可以沿着漫步路径做一些统计工作了，比如求取最大值和最小值

print(walk.min())
print(walk.max())

# 现在来看一个复杂点的统计任务——首次穿越时间，即随机漫步过程中第一次到达某个特定值的时间。假设我们想要知道本次随机漫步需要多久才能距离初始0点至少10步远（任一方向均可）。np.abs(walk)>=10可以得到一个布尔型数组，它表示的是距离
# 是否达到或超过10，而我们想要知道的是第一个10或－10的索引。可以用argmax来解决这个问题，它返回的是该布尔型数组
# 第一个最大值的索引（True就是最大值）

print((np.abs(walk)>= 10).argmax())
# 这里使用argmax并不是很高效，因为它无论如何都会对数组进行完全扫描。在本例中，只要发现了一个True，
# 那我们就知道它是个最大值了。

#一次模拟多个随机漫步
# 如果你希望模拟多个随机漫步过程（比如5000个），只需对上面的代码做一点点修改即可生成所有的随机漫步过程。只要给numpy.random的函数传
# 入一个二元元组就可以产生一个二维数组，然后我们就可以一次性计算5000个随机漫步过程（一行一个）
# 的累计和了

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0,2,size=(nwalks,nsteps))
steps = np.where(draws > 0,1,-1)
walks = steps.cumsum(1)

print(walks)

print(walks.max())
print(walks.min())

# 得到这些数据之后，我们来计算30或－30的最小穿越时间。这里稍微复杂些，因为不是5000个过程都到
# 达了30。我们可以用any方法来对此进行检查

hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
print(hits30.sum())

# 们利用这个布尔型数组选出那些穿越了30（绝对值）的随机漫步（行），并调用argmax在轴1上
# 获取穿越时间

crossing_times = (np.abs(walks[hits30])>=30).argmax(1)
print(crossing_times.mean())

# 请尝试用其他分布方式得到漫步数据。只需使用不同的随机数生成函数即可，
# 如normal用于生成指定均值和标准差的正态分布数据

steps = np.random.normal(loc=0,scale=0.25,size=(nwalks,nsteps))
