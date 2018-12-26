# encoding:utf-8
"""
module: sort.sort_dui : 

@author: mengfei
"""

# 堆排序

import math


def parent(i):
    return math.floor(i / 2)


def left(i):
    return i << 1


def right(i):
    return (i << 1) + 1


print(left(1))
print(right(1))


# 维护队的性质
def max_heapipy(arr, i):
    le = left(i)
    r = right(i)
    if le < len(arr) and arr[le] > arr[i]:
        largest = le
    else:
        largest = i
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        max_heapipy(arr, largest)


a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
max_heapipy(a, 1)
print(a)
