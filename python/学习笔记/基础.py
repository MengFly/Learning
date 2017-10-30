# coding=utf-8
age = 20
name = 'Swaroop'
# 格式化
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python'.format(name))

print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python'.format(name))

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))

# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^12}'.format('hello'))

print('{name} wrote {book}'.format(name='Swaroop',  book='A byte of python'))

#指定print的结尾不是换行符
print('a', end="")
print('b', end='')
print('c', end='\n')

print('This is the first sentence. \
This is the second sentence.')

print( '''Line1
Line2
Line3
''')

# 添加r的时候，在里面的字符都会被原样的输出
print(r'Newlines are indicated by \n')

#Python 是强（Strongly）面向对象的，因为所有的一切都是对象， 包括数字、字符串与函数。


True or True
False and False
not False

# Python 会自动把0、空字符串''、以及None看成为False，其余的都看为true
print('hello', 'python' or 'world')
print('hello', "" or 'world')





