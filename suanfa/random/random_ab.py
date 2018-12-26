# encoding:utf-8
"""
Created on 2017��7��9��

@author: mengfei
"""

import random
import math


# 利用Random01来生成Random(a,b)函数
# 两种方式
# 利用二进制转换成十进制的方式，生成十进制数然后返回，这样生成的每个数的概率是相同的


# 空实现的random01
def random01():
    return random.randint(0, 1)


def random1(a, b):
    k = b - a
    k1 = 1
    c = 0
    # 找到第一个2^n大于k的n
    while k1 <= k:
        c = c + 1
        k1 = k1 * 2
    s = k + 1
    # 生成0到K的数
    while s > k:
        s = 0
        for i in range(c):
            s += random01() * math.pow(2, i)
    return math.floor(s) + a


# print(random1(4, 8))     

# 利用随机移除数组中元素的方式进行返回
# 数组中每个元素移除的概率都是相同的
# 因此最终剩下的那个元素的概率也是相同的

def random2(a, b):
    k = b - a + 1
    number_array = []
    # 获取列表
    for i in range(k):
        number_array.append(i)
    # Copy
    copy_array = number_array[:]
    while len(copy_array) > 1:
        n = len(copy_array)
        for j in range(0, n):
            r = random01()
            if r == 0:
                # 根据下表进行删除列表里面的数据
                del copy_array[n - 1 - j]
        # 如果列表里面的所有数据全部被删除完了，那么就重新进行赋值，删除
        if len(copy_array) == 0:
            copy_array = number_array[:]
    return copy_array[0] + a


print(random1(4, 8))
print(random2(4, 8))
print(random1(4, 8))
print(random2(4, 8))
print(random.randint(4, 9))
print(random.randint(4, 9))
