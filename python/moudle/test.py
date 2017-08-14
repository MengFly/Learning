# -*- coding: cp936 -*-
# 这一行全都是注释
print 'hello,', 'world'
a = 1 # a是整数
print a
a = 'imooc' # a为字符串
print a
# 上面可以随时改变类型的是动态语言
# Java中九尾静态语言，例如int a = 10;

x = 10;
x = x + 10;
print x

# \n 换行， \t制表符 \\表示\本身

s = 'Python was started in 1989 by "Guido"'
print s

# 如果一个字符串包含很多需要转义的字符，可以添加前缀r,里面的字符就不用进行转义了，但里面不能包含'和"
print r'\(~_~)/\(~_~)/'
# 如果要表示多行字符串，可以使用'''...'''来表示
print '''Line1
Line2
Line3
'''
# 可以r和'''...'''一起使用

# 整数 + 浮点数 ==> 浮点数

True or True
False and False
not False

# Python 会自动把0、空字符串''、以及None看成为False，其余的都看为true
print 'hello', 'python' or 'world'
print 'hello', "" or 'world'

# 列表list
# list 是一个有序的列表
['Michael', 'Bob', 'Tracy']

classmates = ['Pmates','Ymates','Lmates']

print classmates

# list 里面不要求是同一种数据类型例如：
listTest = ['test', 234, False]
print listTest

print 'I love',classmates[1], classmates[-1]

# 获取倒数第一位的元素，可以这样
print classmates[-1]

# 添加新元素，使用append添加到末尾
classmates.append('pool')
# 使用insert添加到指定位置
classmates.insert(2, 'haha')
print classmates

# 删除最后一个pop()
classmates.pop()
# 删除某个元素pop(index)
classmates.pop(2)

# 另一种有序列表tuple，tuple一旦被创建就不能被修改了
t = ('bomb','Turing',"JPush")
# 单个元素的tuple创建后面要添加一个逗号，避免和括号的歧义
t = (3,)
t = (2,3,[5, 6])
l = t[2]
l[0] = 'bomb'
l[1] = 'JPush'
print t






