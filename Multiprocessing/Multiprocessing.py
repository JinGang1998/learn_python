#共享内存 shared memory
# 我们可以通过使用Value数据存储在一个共享的内存表中。

import multiprocessing as mp

value1 = mp.Value('i',0)
value2 = mp.Value('d',3.14)
# 其中d和i参数用来设置数据类型的，d表示一个双精浮点类型，i表示一个带符号的整型。


# 在Python的mutiprocessing中，有还有一个Array类，可以和共享内存交互，来实现在进程之间共享数据。
array = mp.Array('i',[1,2,3,4])
# 这里的Array和numpy中的不同，它只能是一维的，不能是多维的。同样和Value 一样，需要定义数据形式，否则会报错。
#各种参数代表的数据类型
# | Type code | C Type             | Python Type       | Minimum size in bytes |
# | --------- | ------------------ | ----------------- | --------------------- |
# | `'b'`     | signed char        | int               | 1                     |
# | `'B'`     | unsigned char      | int               | 1                     |
# | `'u'`     | Py_UNICODE         | Unicode character | 2                     |
# | `'h'`     | signed short       | int               | 2                     |
# | `'H'`     | unsigned short     | int               | 2                     |
# | `'i'`     | signed int         | int               | 2                     |
# | `'I'`     | unsigned int       | int               | 2                     |
# | `'l'`     | signed long        | int               | 4                     |
# | `'L'`     | unsigned long      | int               | 4                     |
# | `'q'`     | signed long long   | int               | 8                     |
# | `'Q'`     | unsigned long long | int               | 8                     |
# | `'f'`     | float              | float             | 4                     |
# | `'d'`     | double             | float             | 8                     |
