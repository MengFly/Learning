# -*- coding: cp936 -*-
# 装饰器

# 函数作用域
# LEGB ： L > E > G > B
# L : local 函数内部作用域
# E : enclosing 函数内部与内嵌函数之间
# G : global 全局作用域
# B : build-in 内置作用域
# 也就是自内向外进行查找

# Python闭包
# 闭包的概念：
# 内部函数中对enclosing作用域的变量进行引用
# 例子：
def func(var) :
    def in_func() :
        return var
    return in_func
f = func(89)
print f     # <function in_func at 0x03081AF0>
print f()   # 89

# 利用闭包我们就可以得到判断时候及格的满分为100和150的两种情况的函数
# 这样我们也就不用去专门编写两个函数了
def set_passline(passline) :
    def cmp(val) :
        if val >= passline :
            print '你及格了，分数为： %d'%val
        else :
            print '你没有及格'
    return cmp
func_100 = set_passline(60) # 判断满分为100的是否及格
func_150 = set_passline(90) # 判断满分为150的是否及格

# 调用函数
func_100(59)    # 你没有及格
func_100(60)    # 你及格了，分数为： 60
func_150(90)    # 你及格了，分数为： 90
func_150(60)    # 你没有及格
# 也就是说闭包的作用就是通过内部函数引用外部函数的enclosing作用域的值从而实现不同功能的函数
# 通过返回这个内部函数我们就可以得到我们想要的函数
# 这样也就减少了代码的书写

# 看下面两个函数（求和和求平均数的函数）
def my_sum(* args) :
    return sum(args)
def my_average(* args) :
    return sum(args) / len(args)
# 但是上面的函数不够完善，因为当没有参数传入或传入字符串的时候就会报错，修改如下：
def my_sum(* args) :
    if len(args) == 0 :
        return 0    # 不传入参数的时候返回0
    for arg in args :
        if not isinstance(arg, int) :
            return 0    # 如果有参数不是整数的也返回0
    return sum(args) 
def my_average(* args) :
    if len(args) == 0 :
        return 0    # 不传入参数的时候返回0
    for arg in args :
        if not isinstance(arg, int) :
            return 0    # 如果有参数不是整数的也返回0
    return sum(args) / len(args)
# 可以看到上面两段代码里面有很多是重复的
# 利用闭包，我们就可以把里面相同的逻辑抽象出来
# 例子：
def dec(func)  :    # 传入的参数是一个函数
    def in_dec(* args) :
        if len(args) == 0 :
            return 0    # 不传入参数的时候返回0
        for arg in args :
            if not isinstance(arg, int) :
                return 0    # 如果有参数不是整数的也返回0
        return func(* args)
    return in_dec
# 里面的dec函数就相当于给dec传入的函数进行了完善，进行了func函数参数的判断
# 调用的时候就可以这样：
def my_sum(* args) :
    return sum(args)
def my_average(* ages) :
    return sum(args)/ len(args)
my_sum = dec(my_sum)
my_average = dec(my_average)
print my_sum()
print my_average()
# 实际上my_sum和my_average实际上就是dec函数里面的in_dec函数例如：
print my_sum.__name__   # in_dec
# 这样就可以动态为函数添加新功能了

# Python 装饰器
# 装饰器用来装饰函数
# 返回一个函数对象
# 被装饰函数标识符指向返回的函数对象
# 装饰器实际上就是简化代码的书写
# 利用上面的代码写一个装饰器的例子：
def dec(func)  :    # 传入的参数是一个函数
    print 'dec call....'
    def in_dec(* args) :
        print 'in_dec call....'
        if len(args) == 0 :
            return 0    # 不传入参数的时候返回0
        for arg in args :
            if not isinstance(arg, int) :
                return 0    # 如果有参数不是整数的也返回0
        return func(* args)
    return in_dec
# 上面的函数添加了几行打印语句。来证明函数的执行
# 下面使用装饰器
@ dec
def my_sum(* args) :
    return sum(args)
# 执行上面的语句，就会输出一句：dec call....
# 说明dec函数被执行了
# 我们再来执行一下my_sum()函数
print my_sum(), my_sum.__name__ # in_dec call.... 0 in_dec
# 说明my_sum()实际上已经变成了in_dec()函数
# 使用装饰器就是简化前面一个例子的代码
# 实际上就相当于my_sum = dec(my_sum)





























