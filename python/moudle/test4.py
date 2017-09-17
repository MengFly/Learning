
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










    
