# -*- coding: cp936 -*-
# Python错误和异常
# 错误： 语法错误（可以被解释器或编译器判断的）， 逻辑错误（例如传参的不合理）无法预判
# 异常： 1、程序遇到逻辑或者算法问题 2、运行过程中计算机错误（内存不够或者IO错误）


# Python的常见的错误

# NameError     当没有定义变量的时候会有这个错误，例如直接在命令行输入a,而没有给a任何定义
# a NameError: name 'a' is not defined

# SyntaxError(语法错误)
# 例如： if len('test') > 0  SyntaxError: invalid syntax
# 这是因为if语句后面要添加:来表示if语句的结束，而上面的语句没有添加:

# IOError 当打开一个不存在的文件的时候会出现这个错误
# 例如 f = open("这个文件肯定不存在.fdsfds")
# IOError: [Errno 2] No such file or directory: '\xd5\xe2\xb8\xf6\xce\xc4\xbc\xfe\xbf\xcf\xb6\xa8\xb2\xbb\xb4\xe6\xd4\xda.fdsfds'

# ZeroDivisionError 除零的错误，当一个数除以零的时候会出现这个错误
# print 3 / 0   ZeroDivisionError: integer division or modulo by zero

# ValueError
# 类型装换的错误
# a = int('aa') ValueError: invalid literal for int() with base 10: 'aa'
# aa字符串没有办法转换为int类型


# 使用 try--except进行异常处理
# try--except相当于Java里面的try--catch
# try :
#   try_suite(可能出现异常的语句)
# except Exception(要捕获的异常)[e](后面可以跟这个变量将异常的类型保存下来)
#   exception_block(捕获异常后执行的语句)
# 例子
try :
    a
except NameError, e :
    print '你a还没有定义就使用了，肯定会触发NameError异常，哈哈，被我捕获到了吧', "而且错误类型是", e

# 如果except后面没有写任何异常的话，就表示捕获任何异常
# 运行前的错误没有办法捕获（例如语法错误，少写一个冒号啊什么的）
# 例子：
try :
    4 / 0
    a
    f = open('这不是一个文件.bushiwenjian')
except :
    print '我特别厉害，任何异常都别想逃过我的法眼'


# 小例子：
# 游戏开始产生一个1-100的随机数
# 用户输入，游戏根据用户输入值提示大或者小
# 用户根据提示继续输入，只到猜中为止
# 如果用户输入错误，程序可以处理异常
import random
def game(num) :
    num_max = 100
    num_min = 0
    while True :
        try :
            guess = int(raw_input('请输入%d-%d的数字'%(num_min, num_max)))
        except ValueError, e :
            print '输入的数值不是一个整数'
            continue
        if guess > num_max or guess < num_min :
            print '请输入数值在%d-%d之的数'%(num_min, num_max)
        elif guess > num :
            num_max = guess
            print '输入的数字大了：', guess
        elif guess < num :
            num_min = guess
            print '输入的数字小了：', guess
        else :
            print '恭喜你答对了, Game Over'
            break
        print '\n'
num = random.randint(0, 100)
# game(num)



# 捕获多个异常
# 在try语句块之下使用多个except语句就可以了
# 例子：
try :
    f = open('1.txt')
    line = f.read(2)    # 这里可能会有IOError
    num = int(line)     # 这里可能有ValueError
    print 'read num is %d'% num
except IOError, e :
    print 'catch IO Error', e
except ValueError, e :
    f.close()
    print 'catch ValueError', e
else :
    f.close()
    print 'No Error'    # 上面两个异常都没有的话就执行下面这个语句


# try--finally语句
# 例子
#try :
#    f = open('1.txt')
#    print int(f.read())
#finally :
#    print 'file close'
    f.close()
# 无论是否有异常finally都会执行
# 没有异常的时候先执行try下面的语句，再执行finally下面的语句
# 有异常的时候先执行finally下面的语句在去处理try下面的异常

# 结合try--except--finally
try :
    f2 = open('2.txt')
    line = f.read(2)    # 这里可能会有IOError
    num = int(line)     # 这里可能有ValueError
    print 'read num is %d'% num
except IOError, e :
    print 'catch IO Error', e
except ValueError, e :
    print 'catch ValueError', e
finally :
    try :
        f2.close()
        print 'f.close()'
    except NameError, e :
        print e
# catch IO Error [Errno 2] No such file or directory: '2.txt'
# f.close()
# name 'f2' is not defined

# try -- except -- else -- finally 结合使用
# 若try语句没有捕获异常，执行完try代码块后，执行else代码段，最后执行finally
# 若try捕获异常，首先执行except处理异常，然后执行finally
try :
    f3 = open('1.txt')
    line = f.read(2)    # 这里可能会有IOError
    num = int(line)     # 这里可能有ValueError
    print 'read num is %d'% num
except IOError, e :
    print 'catch IO Error', e
except ValueError, e :
    print 'catch ValueError', e
else :
    print 'No Error'    # 上面两个异常都没有的话就执行下面这个语句
finally :
    try :
        f3.close()
        print 'file close'
    except NameError, e :
        print e

# with 语句
# with context [as var] :
#     with_suite
# with语句用来代替try--except--finally语句，使代码更加简洁
# context 表达式返回一个对象
# var 用来保存context返回的对象，可以是单个返回值或是一个元组（tuple）
# with_suite使用var变量对context返回的对象进行操作
# 实例：
with open('1.txt') as f4 :
    for line in f4.readlines() :
        print line
# 在whth语句中会自动关闭文件
print f4.closed     # True 说明文件确实已经关闭了，但是我们在with语句里面并没有写文件关闭的语句，它自动替我们关闭了
# 但是当有异常的时候文件就不会正常关闭了
try :
    with open('1.txt') as f5 :
        for line in f5.readlines() :
            print int(line)
except ValueError, e :
    print 'has error'
print f5.closed
# has error
# True
# 说明只要except到Error，那么file也会自动关闭

# with语句实质上是上下文管理
# 1.上下文管理协议： 包含方法__enter__()和__exit__(),支持该协议的对象要实现这两个方法
# 2.上下文管理器：定义执行with语句时要建立的运行时上下文，负责执行with语句上下文的进入与退出操作
# 3.进入上下文管理器：调用管理器__enter__方法，如果设置as var 语句，var变量接收__enter__()方法返回值
# 4.退出上下文管理器：调用__exit__()方法

# 也就是说file对象之所以能在with语句里面使用，就是因为在file这个类定义的时候已经定义好了__enter__()方法和__exit__()方法
# 在as之后会自动调用__enter__()方法，返回一个file对象，可以传给as后面定义的变量
# 在with正常退出或有异常的时候会调用__exit__()方法，在__exit__()方法里面有对文件的关闭的操作

# 例子：自定义一个类，可以在with里面使用
class Mycontext(object) :
    def __init__(self, name) :
        self.name = name

    def __enter__(self) :
        print '__enter__ call...'
        return self

    def do_self(self) :
        print 'do self call...'

    def __exit__(self, exc_type, exc_value, traceback) :
        print '__exit__ call...'
        print 'Error', exc_type, 'info:', exc_value
if __name__ == '__main__' :
    with Mycontext('test context') as m :
        print m.name
        m.do_self()
# __enter__ call...
# test context
# do self call...
# __exit__ call...
# Error None info: None
# 从注释中可以看到先执行__enter__方法，在执行with下面的语句，最后执行__exit__方法

# 加入有一个异常：如下：
try :
    with Mycontext('test context') as m2 :
        int('ds') # 这里有ValueError
        print m.name
        m.do_self()
except ValueError :
    pass
# __enter__ call...
# __exit__ call...
# Error <type 'exceptions.ValueError'> info: invalid literal for int() with base 10: 'ds'
# 说明从有异常的地方开始下面的语句就不会再执行了，直接会执行类的__exit__()方法

# with语句应用场景
# 1. 文件操作
# 2. 进程线程之间互斥对象，例如互斥锁
# 3. 支持上下文的其他对象(实现了__enter__()和__exit__()方法的对象)


# raise语句
# raise语句用于主动抛出异常
# raise语句的语法格式：raise [exception[, args]]
# exception : 异常类   args : 描述异常的元组
# 例子： raise TypeError, '我是这个异常的描述'

# assert语句
# 断言语句： assert语句用于检测表达式是否为真，如果为假则引发AssertionError错误
# 语法格式 : assert epression [, args]
# expression : 表达式  args ： 判断条件的描述信息
# 例如assert 6 == 7 , '6如果不等于7引发异常'  # AssertionError: 6如果不等于7引发异常
# assert 6 == 6 , '6如果不等于7引发异常'  什么也不会输出


# Python标准和自定义 异常
# 标准异常
# BaseException-->
#   KeybordInterrupt(用户中断程序的异常，Ctrl + C)
#   SystemExit(Python 解释器退出)
#   Exception —->
#       SyntaxError, NameError, IOError, ImportError...
# 自定义异常必须继承自Exception类
# 自定义异常只能主动触发（自己抛出后才能捕获）
# 例子：（自定义异常）
class FileError(IOError) :
    pass
# 抛出这个异常的话，就可以raise FileError, 'Test FileError'
# 捕获异常：
try :
    raise FileError, 'Test FileError'
except FileError, e :
    print e     # Test FileError

# 例子：（自定义异常2）
class CustomError(Exception) :
    def __init__(self, info) :
        Exception.__init__(self)
        self.errorinfo = info

    def __str__(self) :
        return "CustomError: %s" % self.errorinfo

# 捕获异常：
try :
    raise CustomError('test CustomError')
except CustomError, e :
    print "ErrorInfo:%s"%e     # ErrorInfo:CustomError: test CustomError


























