# -*- coding: cp936 -*-
# ��һ��ȫ����ע��
print 'hello,', 'world'
a = 1 # a������
print a
a = 'imooc' # aΪ�ַ���
print a
# ���������ʱ�ı����͵��Ƕ�̬����
# Java�о�β��̬���ԣ�����int a = 10;

x = 10;
x = x + 10;
print x

# \n ���У� \t�Ʊ�� \\��ʾ\����

s = 'Python was started in 1989 by "Guido"'
print s

# ���һ���ַ��������ܶ���Ҫת����ַ����������ǰ׺r,������ַ��Ͳ��ý���ת���ˣ������治�ܰ���'��"
print r'\(~_~)/\(~_~)/'
# ���Ҫ��ʾ�����ַ���������ʹ��'''...'''����ʾ
print '''Line1
Line2
Line3
'''
# ����r��'''...'''һ��ʹ��

# ���� + ������ ==> ������

True or True
False and False
not False

# Python ���Զ���0�����ַ���''���Լ�None����ΪFalse������Ķ���Ϊtrue
print 'hello', 'python' or 'world'
print 'hello', "" or 'world'

# �б�list
# list ��һ��������б�
['Michael', 'Bob', 'Tracy']

classmates = ['Pmates','Ymates','Lmates']

print classmates

# list ���治Ҫ����ͬһ�������������磺
listTest = ['test', 234, False]
print listTest

print 'I love',classmates[1], classmates[-1]

# ��ȡ������һλ��Ԫ�أ���������
print classmates[-1]

# �����Ԫ�أ�ʹ��append��ӵ�ĩβ
classmates.append('pool')
# ʹ��insert��ӵ�ָ��λ��
classmates.insert(2, 'haha')
print classmates

# ɾ�����һ��pop()
classmates.pop()
# ɾ��ĳ��Ԫ��pop(index)
classmates.pop(2)

# ��һ�������б�tuple��tupleһ���������Ͳ��ܱ��޸���
t = ('bomb','Turing',"JPush")
# ����Ԫ�ص�tuple��������Ҫ���һ�����ţ���������ŵ�����
t = (3,)
t = (2,3,[5, 6])
l = t[2]
l[0] = 'bomb'
l[1] = 'JPush'
print t






