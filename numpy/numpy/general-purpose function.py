#通用函数（即ufunc）是一种对ndarray中的数据执行元素级运算的函数。你可以将其看做简单函数（接受一个或多个标量值，并产生一个或多个标量值）的矢量化包装器。

# 许多ufunc都是简单的元素级变体，如sqrt和exp
import numpy as np
arr = np.arange(10)

print(arr)
print(np.sqrt(arr))
print(np.exp(arr))
# 这些都是一元（unary）ufunc。

# 另外一些（如add或maximum）接受2个数组（因此也叫二元（binary）ufunc），并返回一个结果数组
x = np.random.randn(8)
y = np.random.randn(8)

print(x)
print(y)
print(np.maximum(x,y))#numpy.maximum计算了x和y中元素级别最大的元素

# 有些ufunc的确可以返回多个数组。modf就是一个例子，它是Python内置函数divmod的矢量化版本，它会返回浮点数数组的小数和整数部分
arr = np.random.randn(7) * 5
print(arr)

remainder,whole_part = np.modf(arr)
print(remainder)
print(whole_part)

# Ufuncs可以接受一个out可选参数，这样就能在数组原地进行操作
print(arr)
print(np.sqrt(arr))
print(np.sqrt(arr,arr))
print(arr)
