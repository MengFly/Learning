# -*- coding: cp936 -*-
# 函数
# 使用help(函数名)来查看函数的用法
help(abs)

cmp(1, 3) # 比较两个数，如果x < y 返回-1， 如果 x > y 返回1, 如果x == y. 返回0

int('123') # 将其他数据转换为整数

str(234) # 将其他类型转换为str

n = 0
N = 100
l = []
while n < N :
    l.append(n * n)
    n = n + 1
print sum(l) # sum计算list里面所有值的和

# 编写函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名，括号，和冒号，然后编写函数体，函数的返回值用return来返回

def my_abs(x) :
    if x > 0 :
        return x
    else :
        return -x
# 如果没有return语句，那么就会返回None

# 返回list列表里面元素的平方和
def square_of_sum(l) :
    n = 0
    for num in l :
        n = n + num * num
    return n
print square_of_sum([23, 44, 56])

# 函数 可以返回多个值
import math
def move(x, y, step, angle) :
	nx = x + step * math.cos(angle)
	ny = y - step + math.sin(angle)
	return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y
# 实际上函数返回的只是一个tuple
print move(100, 100, 60, math.pi / 6) # (151.96152422706632, 40.5)

# 递归函数
def fact(n) :
    if n == 1 :
        return 1
    else :
        return n * fact(n - 1)
print fact(4)

# 定义默认参数 默认参数只能在必须参数后面定义
def power(x, n = 2) :# 默认返回平方
    s = 1
    while n > 0 :
        n = n - 1
        s = s * x
    return s
print power(5)

# 定义可变参数， 如果想让一个函数接收任意个参数，可以定义可变参数
def fn(* args) :
    print args
fn('fds', 89, 'fds')
# 原理就是Python会将这些参数封装成tuple，只要将这些参数看做一个tuple就可以了

# 对list进行切片
listExample = ['Lisa', 'Bomb', 'Tom', 'Bluse', 'Jerry']
# 取前三个元素
listExample[0:3]

#只用一个:,表示从头到尾
listExample[:]

# 将list换成tuple操作完全相同，只是切片结果变成了tuple

# 倒序切片
listExample[-2:]
listExample[:-2]
listExample[-4: -1: 2]
#倒序切片倒数第一个元素是-1， 倒序切片包含其实索引，不包含结束索引

# 对字符串进行切片
# 字符串可以看成是一种list，每个元素就是一个字符。切片结果依旧是字符串
'ABCDEFG'[:3]
'ABCDEFG'[-3:]
'ABCDEFG'[::2] #'ACEG'

# 首字符大写
def toUpperFirst(s) :
	return s[0:1].upper() + s[1:]

# 迭代
# 使用for循环来遍历list和tuple，这种遍历成为迭代
# Python的for循环不仅可以用在tuple和list上面，还可以用在其他任何可迭代的对象上
# 迭代操作就是对于一个集合，无论该集合是有序还是无序，我们用for循环总是可以取出集合的每一个元素
# 目前学习的集合有： list, tuple, str, unicode(有序集合) set(无序集合) dict


# 索引迭代
# 在Python中，迭代永远是取出元素本身，而非元素的索引
# 使用enumerate()函数。可以在for循环中同时绑定索引index和元素name
# 事实上，enumerate()把['Adam', 'Lisa', 'Bart', 'Paul']
# 变成了类似：[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
# 因此迭代的每一个元素实际上是一个tuple
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L) :
    print index, '-', name

for t in enumerate(L) :
	index = t[0]
	name = t[1]
	print index, '-', name

# 迭代dict的value
# dict对象有一个values()方法，这个方法把dict转换成包含所有value的list
d = {'Adam' : 95, 'Lisa' : 85, 'Bart' : 59}
print d.values()

for v in d.values() :
	print v

# dict 除了values()方法，还有一个itervalues()方法，替换values()方法，效果一样
for v in d.itervalues() :
    print v

# values()方法实际上把一个dict转换成了包含value的list
# inervalues()方法不会转换，它会在迭代的过程中依次从dict中取出value，所以inervalues()方法更节省内存
# 如果一个对象说自己可以迭代，那我们就直接用for循环去迭代它，可见，迭代是一种抽象的数据操作，它不对迭代对象内部的数据有任何要求

# 迭代dict的key和value
for key, value in d.items() :
    print key, '-', value
# 和values()相同，items()也有一个对应的iteritems()， iteritems()不占额外内存

# 生成列表
# 要生成list[1,2,3,4,5,6,7,8,9,10], 可以用range(1,11)
range(1, 11)
# 要生成[1x1, 2x2, 3x3,... 10x10]
L = []
for x in range(1, 11) :
    L.append(x * x)
# 使用Python里面特有的列表生成式来生成上面的列表
L2 = [x * x for x in range(1, 11)]
# 把生成的元素x*x 放在前面，后面跟着for循环，就可以把list创建出来

# 复杂表达式
# 可以通过一个复杂的列表生成式把他生成一个HTML表格
d = {'Adam' : 95, 'Lisa' : 85, 'Bart' : 59}
tds = ['<tr><td>%s</td><td>%s</td></tr>' %(name, score) for name, score in d.iteritems()]
# 字符串可以通过%进行格式化，用指定的参数替代%s，字符串的join()方法可以把一个list拼接成一个字符串
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

# 条件过滤
[x * x for x in range(1, 11) if x % 2 == 0]

def funUpListStr(l) :
    return [x.upper() for x in l if isinstance(x, str)]

# 多层表达式
[m + n for m in 'ABC' for n in '123']
# 相当于
L = []
for m in 'ABC' :
    for n in '123' :
        L.append(m + n)

# 生成三个数相同的三位数
print [str(m) + str(n) + str(o) for m in range(0, 10) for n in range(0, 10) for o in range(0, 10) if m == n and m == o]
print [str(m) + str(n) + str(o) for m in range(0, 10) for n in range(0, 10) for o in range(0, 10) if m == o]
