
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










    
