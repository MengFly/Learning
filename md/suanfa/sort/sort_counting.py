# encoding:utf-8
'''
module: sort.sort_counting : 
计数排序
@author: mengfei
'''
import numpy as np
from utils.array_utils import create_random_array
from sort import sort_quick

# 数值排序中的元素满足的条件：
# 元素的范围必须在0-k，并且元素必须为整数
def sort_counting(a, k):
    # 初始化C数组
    c = np.zeros_like(range(k))
    for i in range(len(a)):
        c[a[i]] = c[a[i]] + 1
        # 上面的执行完成之后，C中记录的就是a中对应元素的出现次数
    for i in range(1,len(c)):
        c[i] = c[i] + c[i-1]
        # 上面代码执行完成之后c中记录的就是小于等于a中对应元素的个数
    b = a[:]
    for j in range(len(a))[::-1]:
        b[c[a[j]]-1] = a[j]
        c[a[j]] = c[a[j]] -1
        # 上面两行的代码意思是：
        # 从c中获取比a中元素小于等于的元素的个数，那么这个元素的位置就应该在这个位置
        # 将位置确定之后，就将对应元素小于等于的个数减一，因为如果不减1，下次在遇到同样的元素的时候它还会放在B数组的同一个位置，就起不到排序的作用了
    return b


# test
if __name__ == '__main__':
    # 从这个里面创建的数组在0-100之间，并且全部是整数
    test_arr = create_random_array(100) 
    print(sort_counting(test_arr, 100))
    print(sort_quick.quick_sort(test_arr, 0, len(test_arr)-1))

# print(np.zeros_like(range(10)))
# print(np.zeros(6))

# for i in range(10):
#     print(i)

# for i in range(10)[::-1]:
#     print(i)