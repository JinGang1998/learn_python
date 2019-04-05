import numpy as np

# np.save和np.load是读写磁盘数组数据的两个主要函数。默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为.npy的文件中的
arr = np.arange(10)
np.save('some_array',arr)

print(np.load('some_array.npy'))

# np.savez可以将多个数组保存到一个未压缩文件中，将数组以关键字参数的形式传入即可
np.savez('array_achive.npz',a=arr,b=arr)

arch = np.load('array_archive.npz')
print(arch['b'])

# 如果要将数据压缩，可以使用numpy.savez_compressed
np.savez_compressed('arrays_compressed.npz',a=arr,b=arr)
