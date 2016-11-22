# -*- coding: cp936 -*-
# 变量可以指向一个函数
f = abs
f(-4) # 4
#abs = len
#abs('dfsdf') # 5


# 高阶函数--能接收函数作为参数的一个函数
# 变量可以指向一个函数
# 函数的参数可以接受变量
# 因此一个函数的参数可以接收另一个函数作为参数
def add(x, y, f) :
	return f(x) + f(y)
add(3, 4, abs) # 7


# map()函数
# 它接收一个函数f和一个list，通过f作用于list的每一个元素，返回一个新的list
def f(x) :
    return x * x
print map(f, range(1, 10)) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

def f2(x) :
	return x[0:1].upper() + x[1:]
print map(f2, ['fdsf', 'fdssd', 'fdsfd'])   # ['Fdsf', 'Fdssd', 'Fdsfd']


# reduce()函数 ----参数：函数f(两个参数), list
# 使用f对list每个元素反复调用函数，返回最终值
def f3(x, y) :
    return x + y
print reduce(f3, [1,2,3,4,5]) # 15
# 执行过程 1 + 2 = 3， 3 + 3 = 6， 6 + 4 = 10， 10 + 5 = 15
# reduce() 还可以接收第三个参数，作为计算的初始值
reduce(f3, [1, 2, 3, 4, 5], 10) # 25


#filter() 函数，接收一个函数（返回True或是False）和一个list
# 判断list中的每一项被函数作用后是True还是False，为True则保留，否则去除，最后返回一个新的list
# 例子： 使用filter过滤掉非偶数
def f3(x) :
    return x % 2 == 0
print filter(f3, [4,54,3,3254,54,546,65,3,235,4325]) # [4, 54, 3254, 54, 546]
# 例子，过滤掉空的字符
def is_not_empty(s) :
	return s and len(s.strip()) > 0
print filter(is_not_empty, ['few', ' ', None, "", 'END']) # ['few', 'END']


# 自定义排序函数
# 内置的sorted()函数可以对list进行排序
# sorted()可以接收一个函数来实现自定义排序。
# 传入的函数的定义为：接收两个参数，如果x应该在y前面，则返回-1，如果x应该在y后面则应该返回1，如果x和y相等，返回0
# 例子：
def reversed_cmp(x, y) :
	if x > y :
		return -1
	elif x < y :
		return 1
	else :
		return 0
print sorted([23,42,54,23,654,23,45], reversed_cmp)   # [654, 54, 45, 42, 23, 23, 23]


# 返回函数，函数不仅可以返回基本类型或是list， tuple，dict。。还可以返回函数
# 例子
def f5() :
	print 'call f5()'
	def g() :
		print 'call g()'
	return g # 返回一个函数对象
a = f5() # call f5()
print a # <function g at 0x02FAF670>,说明a只是一个函数对象
a() # call g(),这才是调用了g()

# 例子： 延迟计算
def calc_sum(lst) :
    def lazy_sum() :
        return sum(lst)
    return lazy_sum
f = calc_sum([1,2,3,4])
print f()   # 10
# 不是简单的返回一个数，而是返回一个包含了我们想要的返回值的函数，我们可以随时调用

# 闭包
# 像上面的例子，内层函数引用了外层函数的变量，然后返回内层函数的情况，成为闭包
# 闭包的特点就是返回的函数还引用了外层函数的局部变量，因此，要保证引用的局部变量在函数返回后不能变
# 例子：(这个例子中局部变量就改变了，得不到我们想要的结果)
def count() :
        fs = []
        for i in range(1, 4) :
                def f() :
                        return i * i
                fs.append(f)
        return fs
f1, f2, f3 = count()
# 打印f1(), f2(), f3()会得到什么？是1， 4， 9 吗？实际结果如下
print f1(), f2(), f3()  #9 9 9
# 这是因为当count返回了三个函数的时候，这三个函数所引用的变量i都已经变成了3
# 因此，返回函数不要引用任何循环变量，或者后续会发生变化的变量

# 匿名函数
# 以map为例：
print map(lambda x : x * x, [1,2,3,4,5,6,7,8,9])
# 上面的lambda x : x * x就相当于
# def f(x) :
#       return x * x
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制---只能有一个表达式，不写return，返回值就是表达式的结果
print sorted([25,78,93,32], lambda x, y : -cmp(x, y))
print filter(lambda s : s and len(s.strip()) > 0, ['','f'])

# 装饰器decorator
# 装饰器可以极大地简化代码，避免每个函数编写重复性代码

# 编写无参数decorator
# Python的decorator本质上就是一个高阶函数，他接受一个函数作为参数，然后返回一个新函数
# 使用decorator用Python提供的@ 语法，就可以避免写f = decorator(f)这样的语句
# 例子（为函数提供打印log的功能）
def log(f) :
	def fn(x) :
		print 'call' + f.__name__ + '()...'
		return f(x)
	return fn
@log
def factorial(n) :
	return reduce(lambda x, y : x * y, range(1, n + 1))
print factorial(10)     #callfactorial()...3628800
#log()为函数添加打印log的功能，使用@log就相当于f = log(f)

# 要让@log可以适应于任何参数定义的函数，可以使用Python的*args和**kw，保证任意个参数总是能正常调用
def log(f) :
	def fn(*args, **kw) :
		print 'call' + f.__name__ + '()...'
		return f(*args, **kw)
	return fn
@log
def add(x, y) :
        return x + y
print add(2, 4)         #calladd()...6

# 编写带参数的decorator
# 上面定义的log函数打印的log是定义好的，函数名()...,如果想要自定义log语句，可以为decorator定义参数
# 例子：
def log(prefix) :
	def log_decorator(f) :
		def wrapper(*args, **kw) :
			print '[%s]%s()...' %(prefix, f.__name__)
			return f(*args, **kw)
		return wrapper
	return log_decorator
# 调用
def test() :
	print 'test'
print test()
#[DEBUG]test()...
#test
#None

# 完善decorator
# @decotator虽然会动态地为函数增加功能，但是现在的函数已经不是之前我们定义的函数了，例如打印test的函数名
print test.__name__     #wrapper
# 可以发现函数确实已经不是我们之前定义的函数了
# 因此我们要把原函数的一些属性复制到新函数中
# 例子：
def log(f) :
        def wrapper(*args, **kw) :
                print 'call... '
                return f(*args, **kw)
        wrapper.__name__ = f.__name__
        wrapper.__doc__ = f.__doc__
        return wrapper
# 这样写decorator很不方便，因为我们也很难把原函数的所有属性一个一个复制到新函数上，所以Python内置的functools可以用来自动化这种“复制任务”
# 例子：
import functools
def log(f) :
	@functools.wraps(f)
	def wrapper(*args, **kw) :
		print 'call...'
		return f(*args, **kw)
	return wrapper

## 最终完善的例子
def log(prefix) :
        def log_decrator(f) :
                @functools.wraps(f)
                def wrapper(*args, **kw) :
                        print '[%s]call %s()... ' %(prefix, f.__name__)
                        return f(*args, **kw)
                return wrapper
        return log_decrator
@log('DEBUG')
def test(x) :
	print 'love pyl'

print test(2)
print test.__name__
print test.__doc__

# 偏函数
# 例如int()函数会把字符串转换为10进制的数。如果想要转换为8进制的数，可以这样调用
int('234555', base=8)   # 80237
# 单每一次都要写base = 8，太麻烦，我们可以这样定义一个函数
import functools
int2 = functools.partial(int, base = 8)
int2('234555')  # 80237
# 这样生成的int2函数，就是int(x, base=8)
# 也就简便了函数的调用









    
