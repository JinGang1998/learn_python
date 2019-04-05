# 线性代数（如矩阵乘法、矩阵分解、行列式以及其他方阵数学等）是任何数组库的重要
# 组成部分。不像某些语言（如MATLAB），通过*对两个二维数组相乘得到的是一个元素级的积，而不是
# 一个矩阵点积。因此，NumPy提
# 供了一个用于矩阵乘法的dot函数（既是一个数组方法也是numpy命名空间中的一个函数）
import numpy as np

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x)
print(y)
print(x.dot(y))

#x.dot(y) 等价于  np.dot(x,y)

print(np.dot(x,y))

# 一个二维数组跟一个大小合适的一维数组的矩阵点积运算之后将会得到一个一维数组
print(np.ones(3))
print(np.dot(x,np.ones(3)))

# @符（类似Python 3.5）也可以用作中缀运算符，进行矩阵乘法
print(x @ np.ones(3))


# numpy.linalg中有一组标准的矩阵分解运算以及诸如求逆和行列式之类的东西。它们
# 跟MATLAB和R等语言所使用的是相同的行业标准线性代数库，如BLAS、LAPACK、
# Intel MKL（Math Kernel Library，可能有，取决于你的NumPy版本）

from numpy.linalg import inv,qr
X = np.random.randn(5,5)
mat = X.T.dot(X)
print(inv(mat))
print(mat.dot(inv(mat)))
q ,r = qr(mat)
print(r)
# 表达式X.T.dot(X)计算X和它的转置X.T的点积
