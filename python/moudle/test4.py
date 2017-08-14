# -*- coding: cp936 -*-
# ��������ָ��һ������
f = abs
f(-4) # 4
#abs = len
#abs('dfsdf') # 5


# �߽׺���--�ܽ��պ�����Ϊ������һ������
# ��������ָ��һ������
# �����Ĳ������Խ��ܱ���
# ���һ�������Ĳ������Խ�����һ��������Ϊ����
def add(x, y, f) :
	return f(x) + f(y)
add(3, 4, abs) # 7


# map()����
# ������һ������f��һ��list��ͨ��f������list��ÿһ��Ԫ�أ�����һ���µ�list
def f(x) :
    return x * x
print map(f, range(1, 10)) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

def f2(x) :
	return x[0:1].upper() + x[1:]
print map(f2, ['fdsf', 'fdssd', 'fdsfd'])   # ['Fdsf', 'Fdssd', 'Fdsfd']


# reduce()���� ----����������f(��������), list
# ʹ��f��listÿ��Ԫ�ط������ú�������������ֵ
def f3(x, y) :
    return x + y
print reduce(f3, [1,2,3,4,5]) # 15
# ִ�й��� 1 + 2 = 3�� 3 + 3 = 6�� 6 + 4 = 10�� 10 + 5 = 15
# reduce() �����Խ��յ�������������Ϊ����ĳ�ʼֵ
reduce(f3, [1, 2, 3, 4, 5], 10) # 25


#filter() ����������һ������������True����False����һ��list
# �ж�list�е�ÿһ��������ú���True����False��ΪTrue����������ȥ������󷵻�һ���µ�list
# ���ӣ� ʹ��filter���˵���ż��
def f3(x) :
    return x % 2 == 0
print filter(f3, [4,54,3,3254,54,546,65,3,235,4325]) # [4, 54, 3254, 54, 546]
# ���ӣ����˵��յ��ַ�
def is_not_empty(s) :
	return s and len(s.strip()) > 0
print filter(is_not_empty, ['few', ' ', None, "", 'END']) # ['few', 'END']


# �Զ���������
# ���õ�sorted()�������Զ�list��������
# sorted()���Խ���һ��������ʵ���Զ�������
# ����ĺ����Ķ���Ϊ�������������������xӦ����yǰ�棬�򷵻�-1�����xӦ����y������Ӧ�÷���1�����x��y��ȣ�����0
# ���ӣ�
def reversed_cmp(x, y) :
	if x > y :
		return -1
	elif x < y :
		return 1
	else :
		return 0
print sorted([23,42,54,23,654,23,45], reversed_cmp)   # [654, 54, 45, 42, 23, 23, 23]


# ���غ����������������Է��ػ������ͻ���list�� tuple��dict���������Է��غ���
# ����
def f5() :
	print 'call f5()'
	def g() :
		print 'call g()'
	return g # ����һ����������
a = f5() # call f5()
print a # <function g at 0x02FAF670>,˵��aֻ��һ����������
a() # call g(),����ǵ�����g()

# ���ӣ� �ӳټ���
def calc_sum(lst) :
    def lazy_sum() :
        return sum(lst)
    return lazy_sum
f = calc_sum([1,2,3,4])
print f()   # 10
# ���Ǽ򵥵ķ���һ���������Ƿ���һ��������������Ҫ�ķ���ֵ�ĺ��������ǿ�����ʱ����

# �հ�
# ����������ӣ��ڲ㺯����������㺯���ı�����Ȼ�󷵻��ڲ㺯�����������Ϊ�հ�
# �հ����ص���Ƿ��صĺ�������������㺯���ľֲ���������ˣ�Ҫ��֤���õľֲ������ں������غ��ܱ�
# ���ӣ�(��������оֲ������͸ı��ˣ��ò���������Ҫ�Ľ��)
def count() :
        fs = []
        for i in range(1, 4) :
                def f() :
                        return i * i
                fs.append(f)
        return fs
f1, f2, f3 = count()
# ��ӡf1(), f2(), f3()��õ�ʲô����1�� 4�� 9 ��ʵ�ʽ������
print f1(), f2(), f3()  #9 9 9
# ������Ϊ��count����������������ʱ�����������������õı���i���Ѿ������3
# ��ˣ����غ�����Ҫ�����κ�ѭ�����������ߺ����ᷢ���仯�ı���

# ��������
# ��mapΪ����
print map(lambda x : x * x, [1,2,3,4,5,6,7,8,9])
# �����lambda x : x * x���൱��
# def f(x) :
#       return x * x
# �ؼ���lambda��ʾ����������ð��ǰ���x��ʾ��������
# ���������и�����---ֻ����һ�����ʽ����дreturn������ֵ���Ǳ��ʽ�Ľ��
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

# ƫ����
# ����int()��������ַ���ת��Ϊ10���Ƶ����������Ҫת��Ϊ8���Ƶ�����������������
int('234555', base=8)   # 80237
# ��ÿһ�ζ�Ҫдbase = 8��̫�鷳�����ǿ�����������һ������
import functools
int2 = functools.partial(int, base = 8)
int2('234555')  # 80237
# �������ɵ�int2����������int(x, base=8)
# Ҳ�ͼ���˺����ĵ���









    
