# numpy.random模块对Python内置的random进行了补充，增加了一些用于高效生成多种概率分布的样
# 本值的函数。例如，你可以用normal来得到一个标准正态分布的4×4样本数组
import numpy as np

samples = np.random.normal(size=(4,4))
print(samples)

# Python内置的random模块则只能一次生成一个样本值。从下面的测试结果中可以看出，
# 如果需要产生大量样本值，numpy.random快了不止一个数量级

from random import normalvariate

N = 1000000
# %timeit samples = [normalvariate(0,1) for _ in range(N)]
# %timeit np.random.normal(size=N)

# 我们说这些都是伪随机数，是因为它们都是通过算法基于随机数生成器种子，在确定性的条件下生成的。
# 你可以用NumPy的np.random.seed更改随机数生成种子
np.random.seed(1234)

# random的数据生成函数使用了全局的随机种子。要避免全局状态，你可以使用numpy.random.RandomState，
# 创建一个与其它隔离的随机数生成器
rng = np.random.RandomState(1234)
print(rng.randn(10))
