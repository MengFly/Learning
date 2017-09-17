
print sorted([25,78,93,32], lambda x, y : -cmp(x, y))
print filter(lambda s : s and len(s.strip()) > 0, ['','f'])

# װ����decorator
# װ�������Լ���ؼ򻯴��룬����ÿ��������д�ظ��Դ���

# ��д�޲���decorator
# Python��decorator�����Ͼ���һ���߽׺�����������һ��������Ϊ������Ȼ�󷵻�һ���º���
# ʹ��decorator��Python�ṩ��@ �﷨���Ϳ��Ա���дf = decorator(f)���������
# ���ӣ�Ϊ�����ṩ��ӡlog�Ĺ��ܣ�
def log(f) :
	def fn(x) :
		print 'call' + f.__name__ + '()...'
		return f(x)
	return fn
@log
def factorial(n) :
	return reduce(lambda x, y : x * y, range(1, n + 1))
print factorial(10)     #callfactorial()...3628800
#log()Ϊ������Ӵ�ӡlog�Ĺ��ܣ�ʹ��@log���൱��f = log(f)

# Ҫ��@log������Ӧ���κβ�������ĺ���������ʹ��Python��*args��**kw����֤�����������������������
def log(f) :
	def fn(*args, **kw) :
		print 'call' + f.__name__ + '()...'
		return f(*args, **kw)
	return fn
@log
def add(x, y) :
        return x + y
print add(2, 4)         #calladd()...6

# ��д��������decorator
# ���涨���log������ӡ��log�Ƕ���õģ�������()...,�����Ҫ�Զ���log��䣬����Ϊdecorator�������
# ���ӣ�
def log(prefix) :
	def log_decorator(f) :
		def wrapper(*args, **kw) :
			print '[%s]%s()...' %(prefix, f.__name__)
			return f(*args, **kw)
		return wrapper
	return log_decorator
# ����
def test() :
	print 'test'
print test()
#[DEBUG]test()...
#test
#None

# ����decorator
# @decotator��Ȼ�ᶯ̬��Ϊ�������ӹ��ܣ��������ڵĺ����Ѿ�����֮ǰ���Ƕ���ĺ����ˣ������ӡtest�ĺ�����
print test.__name__     #wrapper
# ���Է��ֺ���ȷʵ�Ѿ���������֮ǰ����ĺ�����
# �������Ҫ��ԭ������һЩ���Ը��Ƶ��º�����
# ���ӣ�
def log(f) :
        def wrapper(*args, **kw) :
                print 'call... '
                return f(*args, **kw)
        wrapper.__name__ = f.__name__
        wrapper.__doc__ = f.__doc__
        return wrapper
# ����дdecorator�ܲ����㣬��Ϊ����Ҳ���Ѱ�ԭ��������������һ��һ�����Ƶ��º����ϣ�����Python���õ�functools���������Զ������֡���������
# ���ӣ�
import functools
def log(f) :
	@functools.wraps(f)
	def wrapper(*args, **kw) :
		print 'call...'
		return f(*args, **kw)
	return wrapper

## �������Ƶ�����
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










    
