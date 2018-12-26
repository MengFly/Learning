# encoding:utf-8
"""
module: sort.sort_quick : 
快速排序，以及一些相关的操作
@author: mengfei
"""
from numpy import random
from suanfa.utils.array_utils import create_random_array


# 找出主元的位置，并根据主元的位置进行简单排序
def partition(a, p, r):
    # 主元设定为元素的最后一个
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    temp = a[i + 1]
    a[i + 1] = a[r]
    a[r] = temp
    return i + 1


# 快速排序，排序的基本思想
# 从要进行排序的数组里面找出一个“主元”
# 对这个主元进行排序，使得：
# 在主元左侧的元素都小于这个主元
# 在主元右侧的元素都大于这个主元
# 之后再对主元左侧和右侧的两部分做同样的操作
# 当所有操作完成的时候数组就已经拍好了顺序
def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)
    return a


# 将最后一个元素和随机的位置交换，达到主元是随机位置的目的
def randomized_partition(a, p, r):
    i = random.randint(p, r + 1)
    temp = a[r]
    a[r] = a[i]
    a[i] = temp
    return partition(a, p, r)


# 主元是随机的位置的数值
def randomized_quick_sort(a, p, r):
    if p < r:
        q = randomized_partition(a, p, r)
        randomized_quick_sort(a, p, q - 1)
        randomized_quick_sort(a, q + 1, r)
    return a


# test
if __name__ == '__main__':
    test_arr = create_random_array(100)
    print(quick_sort(test_arr, 0, len(test_arr) - 1))
    print(randomized_quick_sort(test_arr, 0, len(test_arr) - 1))
