# -*- coding: cp936 -*-
# Python������쳣
# ���� �﷨���󣨿��Ա���������������жϵģ��� �߼��������紫�εĲ������޷�Ԥ��
# �쳣�� 1�����������߼������㷨���� 2�����й����м���������ڴ治������IO����


# Python�ĳ����Ĵ���

# NameError     ��û�ж��������ʱ����������������ֱ��������������a,��û�и�a�κζ���
# a NameError: name 'a' is not defined

# SyntaxError(�﷨����)
# ���磺 if len('test') > 0  SyntaxError: invalid syntax
# ������Ϊif������Ҫ���:����ʾif���Ľ���������������û�����:

# IOError ����һ�������ڵ��ļ���ʱ�������������
# ���� f = open("����ļ��϶�������.fdsfds")
# IOError: [Errno 2] No such file or directory: '\xd5\xe2\xb8\xf6\xce\xc4\xbc\xfe\xbf\xcf\xb6\xa8\xb2\xbb\xb4\xe6\xd4\xda.fdsfds'

# ZeroDivisionError ����Ĵ��󣬵�һ�����������ʱ�������������
# print 3 / 0   ZeroDivisionError: integer division or modulo by zero

# ValueError
# ����װ���Ĵ���
# a = int('aa') ValueError: invalid literal for int() with base 10: 'aa'
# aa�ַ���û�а취ת��Ϊint����


# ʹ�� try--except�����쳣����
# try--except�൱��Java�����try--catch
# try :
#   try_suite(���ܳ����쳣�����)
# except Exception(Ҫ������쳣)[e](������Ը�����������쳣�����ͱ�������)
#   exception_block(�����쳣��ִ�е����)
# ����
try :
    a
except NameError, e :
    print '��a��û�ж����ʹ���ˣ��϶��ᴥ��NameError�쳣�����������Ҳ����˰�', "���Ҵ���������", e

# ���except����û��д�κ��쳣�Ļ����ͱ�ʾ�����κ��쳣
# ����ǰ�Ĵ���û�а취���������﷨������дһ��ð�Ű�ʲô�ģ�
# ���ӣ�
try :
    4 / 0
    a
    f = open('�ⲻ��һ���ļ�.bushiwenjian')
except :
    print '���ر��������κ��쳣�������ӹ��ҵķ���'


# С���ӣ�
# ��Ϸ��ʼ����һ��1-100�������
# �û����룬��Ϸ�����û�����ֵ��ʾ�����С
# �û�������ʾ�������룬ֻ������Ϊֹ
# ����û�������󣬳�����Դ����쳣
import random
def game(num) :
    num_max = 100
    num_min = 0
    while True :
        try :
            guess = int(raw_input('������%d-%d������'%(num_min, num_max)))
        except ValueError, e :
            print '�������ֵ����һ������'
            continue
        if guess > num_max or guess < num_min :
            print '��������ֵ��%d-%d֮����'%(num_min, num_max)
        elif guess > num :
            num_max = guess
            print '��������ִ��ˣ�', guess
        elif guess < num :
            num_min = guess
            print '���������С�ˣ�', guess
        else :
            print '��ϲ������, Game Over'
            break
        print '\n'
num = random.randint(0, 100)
# game(num)



# �������쳣
# ��try����֮��ʹ�ö��except���Ϳ�����
# ���ӣ�
try :
    f = open('1.txt')
    line = f.read(2)    # ������ܻ���IOError
    num = int(line)     # ���������ValueError
    print 'read num is %d'% num
except IOError, e :
    print 'catch IO Error', e
except ValueError, e :
    f.close()
    print 'catch ValueError', e
else :
    f.close()
    print 'No Error'    # ���������쳣��û�еĻ���ִ������������


# try--finally���
# ����
#try :
#    f = open('1.txt')
#    print int(f.read())
#finally :
#    print 'file close'
    f.close()
# �����Ƿ����쳣finally����ִ��
# û���쳣��ʱ����ִ��try�������䣬��ִ��finally��������
# ���쳣��ʱ����ִ��finally����������ȥ����try������쳣

# ���try--except--finally
try :
    f2 = open('2.txt')
    line = f.read(2)    # ������ܻ���IOError
    num = int(line)     # ���������ValueError
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

# try -- except -- else -- finally ���ʹ��
# ��try���û�в����쳣��ִ����try������ִ��else����Σ����ִ��finally
# ��try�����쳣������ִ��except�����쳣��Ȼ��ִ��finally
try :
    f3 = open('1.txt')
    line = f.read(2)    # ������ܻ���IOError
    num = int(line)     # ���������ValueError
    print 'read num is %d'% num
except IOError, e :
    print 'catch IO Error', e
except ValueError, e :
    print 'catch ValueError', e
else :
    print 'No Error'    # ���������쳣��û�еĻ���ִ������������
finally :
    try :
        f3.close()
        print 'file close'
    except NameError, e :
        print e

# with ���
# with context [as var] :
#     with_suite
# with�����������try--except--finally��䣬ʹ������Ӽ��
# context ���ʽ����һ������
# var ��������context���صĶ��󣬿����ǵ�������ֵ����һ��Ԫ�飨tuple��
# with_suiteʹ��var������context���صĶ�����в���
# ʵ����
with open('1.txt') as f4 :
    for line in f4.readlines() :
        print line
# ��whth����л��Զ��ر��ļ�
print f4.closed     # True ˵���ļ�ȷʵ�Ѿ��ر��ˣ�����������with������沢û��д�ļ��رյ���䣬���Զ������ǹر���
# ���ǵ����쳣��ʱ���ļ��Ͳ��������ر���
try :
    with open('1.txt') as f5 :
        for line in f5.readlines() :
            print int(line)
except ValueError, e :
    print 'has error'
print f5.closed
# has error
# True
# ˵��ֻҪexcept��Error����ôfileҲ���Զ��ر�

# with���ʵ�����������Ĺ���
# 1.�����Ĺ���Э�飺 ��������__enter__()��__exit__(),֧�ָ�Э��Ķ���Ҫʵ������������
# 2.�����Ĺ�����������ִ��with���ʱҪ����������ʱ�����ģ�����ִ��with��������ĵĽ������˳�����
# 3.���������Ĺ����������ù�����__enter__�������������as var ��䣬var��������__enter__()��������ֵ
# 4.�˳������Ĺ�����������__exit__()����

# Ҳ����˵file����֮��������with�������ʹ�ã�������Ϊ��file����ඨ���ʱ���Ѿ��������__enter__()������__exit__()����
# ��as֮����Զ�����__enter__()����������һ��file���󣬿��Դ���as���涨��ı���
# ��with�����˳������쳣��ʱ������__exit__()��������__exit__()���������ж��ļ��ĹرյĲ���

# ���ӣ��Զ���һ���࣬������with����ʹ��
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
# ��ע���п��Կ�����ִ��__enter__��������ִ��with�������䣬���ִ��__exit__����

# ������һ���쳣�����£�
try :
    with Mycontext('test context') as m2 :
        int('ds') # ������ValueError
        print m.name
        m.do_self()
except ValueError :
    pass
# __enter__ call...
# __exit__ call...
# Error <type 'exceptions.ValueError'> info: invalid literal for int() with base 10: 'ds'
# ˵�������쳣�ĵط���ʼ��������Ͳ�����ִ���ˣ�ֱ�ӻ�ִ�����__exit__()����

# with���Ӧ�ó���
# 1. �ļ�����
# 2. �����߳�֮�以��������绥����
# 3. ֧�������ĵ���������(ʵ����__enter__()��__exit__()�����Ķ���)


# raise���
# raise������������׳��쳣
# raise�����﷨��ʽ��raise [exception[, args]]
# exception : �쳣��   args : �����쳣��Ԫ��
# ���ӣ� raise TypeError, '��������쳣������'

# assert���
# ������䣺 assert������ڼ����ʽ�Ƿ�Ϊ�棬���Ϊ��������AssertionError����
# �﷨��ʽ : assert epression [, args]
# expression : ���ʽ  args �� �ж�������������Ϣ
# ����assert 6 == 7 , '6���������7�����쳣'  # AssertionError: 6���������7�����쳣
# assert 6 == 6 , '6���������7�����쳣'  ʲôҲ�������


# Python��׼���Զ��� �쳣
# ��׼�쳣
# BaseException-->
#   KeybordInterrupt(�û��жϳ�����쳣��Ctrl + C)
#   SystemExit(Python �������˳�)
#   Exception ��->
#       SyntaxError, NameError, IOError, ImportError...
# �Զ����쳣����̳���Exception��
# �Զ����쳣ֻ�������������Լ��׳�����ܲ���
# ���ӣ����Զ����쳣��
class FileError(IOError) :
    pass
# �׳�����쳣�Ļ����Ϳ���raise FileError, 'Test FileError'
# �����쳣��
try :
    raise FileError, 'Test FileError'
except FileError, e :
    print e     # Test FileError

# ���ӣ����Զ����쳣2��
class CustomError(Exception) :
    def __init__(self, info) :
        Exception.__init__(self)
        self.errorinfo = info

    def __str__(self) :
        return "CustomError: %s" % self.errorinfo

# �����쳣��
try :
    raise CustomError('test CustomError')
except CustomError, e :
    print "ErrorInfo:%s"%e     # ErrorInfo:CustomError: test CustomError


























