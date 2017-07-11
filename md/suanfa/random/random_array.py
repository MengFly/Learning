# encoding:utf-8
'''
module: s_random.random_array : 

@author: mengfei
'''

import random
import math

# 以下的两种对数组进行随机排列的算法所得出的每一种结果在概率上面都是相同的

'''
 对随机的数组进行排序，根据给数组配置优先级进行随机排序
'''
def permute_by_sorting(a):
    n = len(a)
    sort_key_a = []
    # 先获取一个优先级比较的数列。这个数列长度和要进行排序的数列是相同的，对应位置对应要进行排列的数组的每一项
    for i in range(n):
        sort_key_a.append(random.randint(0, math.pow(n, 3)))
    # sort A using sort_key_a
    for i in range(1,n):
        if(sort_key_a[i] > sort_key_a[i-1]):
            swap = a[i]
            a[i] = a[i-1]
            a[i-1] = swap
    return a
   
# 原址排列给定数组
def randomize_in_place(a):
    n = len(a)
    for i in range(n):
        index_swap = random.randint(i, n-1)
        swap = a[i]
        a[i] = a[index_swap]
        a[index_swap] = swap
    return a

a = [1,2,3,4,5,6,7,8,9,0]

print(randomize_in_place(a))
print(permute_by_sorting(a))
    
'''
在线雇佣问题：
算法结构：
先面试前k个前面面试的人
获得面试分数最高的一个人的分数
但这k个人都不录用
之后面试后面的人，一旦有人面试的分比前面的人的分数高，那么就录用这个人
理论上来说，当k=n/e的时候我们雇佣到最好的应聘者的概率是最大的
'''
def on_line_maximum(a, k=len(a)/math.e):
    k = math.floor(k)
    bestscore = -1
    n = len(a)
    # 选出前k个里面最好的那个人
    for i in range(k):
        if(a[i] > bestscore):
            bestscore = a[i]
    # 剩下的人里面，一旦存在比之前最好的人，就留下来
    for i in range(k+1, n):
        if a[i] > bestscore :
            return a[i]
    return a[n-1]
    
# 使用随机的数列进行测试
d = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0
    }

# d[3] = 1
# print(d[3])

# 测试10000个数据
for i in range(10000):
    n = on_line_maximum(randomize_in_place(a))
#     print(n)、
    value = int(d.get(n)) + 1
    d[n] = value

for n in d:
    print("%d 的选中比例为 %.2f%%" %(n, d.get(n)/10000*100))

'''
经过测试发现：
获取最好的应聘者的概率大概在36%
获取次等的应聘者概率大概在20%
获取第三等的应聘者概率大概在12%
因此可以发现能得到较好的应聘者的概率还是特别大的，占到了将近七成的概率。

下面以取自一次的测试：
0 的选中比例为 3.74%
1 的选中比例为 3.76%
2 的选中比例为 3.86%
3 的选中比例为 3.73%
4 的选中比例为 3.82%
5 的选中比例为 5.05%
6 的选中比例为 7.29%
7 的选中比例为 11.29%
8 的选中比例为 20.34%
9 的选中比例为 37.12%
'''

def get_show(d):
    a = []
    b = []
    for key in d:
        a.append(key)
        b.append(d.get(key)/10000)
    return a,b

import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题 
plt.title(u"on_line_maximum算法雇佣人员质量分布")    
plt.xlabel(u"人员质量")
plt.ylabel(u"所占百分比")
plt.bar(get_show(d)[0], get_show(d)[1], 0.3)
plt.show()

#比例图参见 on_line_maximum算法雇佣人员质量分布.PNG