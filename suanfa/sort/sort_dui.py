# encoding:utf-8
'''
module: sort.sort_dui : 

@author: mengfei
'''

# 堆排序

import math
def parent(i):
    return math.floor(i/2)

def left(i):
    return  i << 1

def right(i):
    return (i << 1) + 1

print(left(1))
print(right(1))


# 维护队的性质
def max_heapipy(a, i):
    l = left(i)
    r = right(i)
    if (l < len(a) and a[l] > a[i]):
        largest = l
    else :
        largest = i
    if r < len(a) and a[r] > a[largest] :
        largest = r
    if largest != i:
        temp = a[i]
        a[i] = a[largest]
        a[largest] = temp
        max_heapipy(a, largest)


a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1];
max_heapipy(a, 1)
print(a)
    