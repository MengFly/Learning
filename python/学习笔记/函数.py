def say(message, times=1):
             print(message * times)

say('Hello')
say('World', 5)

def func(a, b=5, c=10):
             print(' a is ', a, ' and b is ', b, ' and c is ', c)

func(3, 7)
func(25, c=39)
func(c=34, a=1)


# 当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数（Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。
# 类似地，当我们声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字参数都将被收集并汇集成一个名为 param 的字典（Dictionary）。
def total(a=5, *numbers, **phonebook):
             '''这个函数用来获取函数的各种参数
             其中，
             当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数（Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。
             类似地，当我们声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字参数都将被收集并汇集成一个名为 param 的字典（Dictionary）。
             '''
             print('a', a)

             #遍历元组中的所有项目
             for single_item in numbers:
                          print('single_item ', single_item)

             # 遍历字典中的所有项目
             for first_part, second_part in phonebook.items():
                          print(first_part, second_part)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))


print(total.__doc__)


# 返回两个不同的值
def get_error_details():
             return (2, 'second error details')
errnum, errstr  = get_error_details()
print(errnum, errstr)


# Lambda形式
# lambda 语句用来创建函数对象。
#本质上，lambda 需要一个参数，后面仅跟单个表达式作为函数体，而表达式的值被这个新建的函数返回
def make_repeater(n):
             return lambda s: s* n
twice = make_repeater(2)
print(twice("word"))
print(twice(5))

# 递归函数
def fact(n) :
    if n == 1 :
        return 1
    else :
        return n * fact(n - 1)


# 高阶函数--能接收函数作为参数的一个函数
# 变量可以指向一个函数
# 函数的参数可以接受变量
# 因此一个函数的参数可以接收另一个函数作为参数
def add(x, y, f) :
	return f(x) + f(y)
add(3, 4, abs) # 7


def f2(x) :
	return x[0:1].upper() + x[1:]
print map(f2, ['fdsf', 'fdssd', 'fdsfd'])   # ['Fdsf', 'Fdssd', 'Fdsfd']


#filter() 函数，接收一个函数（返回True或是False）和一个list
# 判断list中的每一项被函数作用后是True还是False，为True则保留，否则去除，最后返回一个新的list
# 例子： 使用filter过滤掉非偶数
def f3(x) :
    return x % 2 == 0
print filter(f3, [4,54,3,3254,54,546,65,3,235,4325]) # [4, 54, 3254, 54, 546]


# 返回函数，函数不仅可以返回基本类型或是list， tuple，dict。。还可以返回函数
# 例子
def f5() :
	print 'call f5()'
	def g() :
		print 'call g()'
	return g # 返回一个函数对象
a = f5() # call f5()



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
#因此，返回函数不要引用任何循环变量，或者后续会发生变化的变量



# 匿名函数
# 以map为例：
print map(lambda x : x * x, [1,2,3,4,5,6,7,8,9])
# 上面的lambda x : x * x就相当于
# def f(x) :
#       return x * x
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制---只能有一个表达式，不写return，返回值就是表达式的结果



# 偏函数
# 例如int()函数会把字符串转换为10进制的数。如果想要转换为8进制的数，可以这样调用
int('234555', base=8)   # 80237
# 单每一次都要写base = 8，太麻烦，我们可以这样定义一个函数
import functools
int2 = functools.partial(int, base = 8)
int2('234555')  # 80237
# 这样生成的int2函数，就是int(x, base=8)
# 也就简便了函数的调用


