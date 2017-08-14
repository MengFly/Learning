# encoding:utf-8
'''
module: utils.array_utils : 
提供一些数组的工具方法
@author: mengfei
'''
from numpy import random

def create_random_array(length):
    a = []
    for i in range(length):
        a.append(random.randint(length))
    return a

# test
if __name__ == '__main__' :
    print(create_random_array(100))