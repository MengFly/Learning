# -*- coding: cp936 -*-
# ����
# ʹ��help(������)���鿴�������÷�
help(abs)

cmp(1, 3) # �Ƚ������������x < y ����-1�� ��� x > y ����1, ���x == y. ����0

int('123') # ����������ת��Ϊ����

str(234) # ����������ת��Ϊstr

n = 0
N = 100
l = []
while n < N :
    l.append(n * n)
    n = n + 1
print sum(l) # sum����list��������ֵ�ĺ�

# ��д����
# ��Python�У�����һ������Ҫʹ��def��䣬����д�������������ţ���ð�ţ�Ȼ���д�����壬�����ķ���ֵ��return������

def my_abs(x) :
    if x > 0 :
        return x
    else :
        return -x
# ���û��return��䣬��ô�ͻ᷵��None

# ����list�б�����Ԫ�ص�ƽ����
def square_of_sum(l) :
    n = 0
    for num in l :
        n = n + num * num
    return n
print square_of_sum([23, 44, 56])

# ���� ���Է��ض��ֵ
import math
def move(x, y, step, angle) :
	nx = x + step * math.cos(angle)
	ny = y - step + math.sin(angle)
	return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y
# ʵ���Ϻ������ص�ֻ��һ��tuple
print move(100, 100, 60, math.pi / 6) # (151.96152422706632, 40.5)

# �ݹ麯��
def fact(n) :
    if n == 1 :
        return 1
    else :
        return n * fact(n - 1)
print fact(4)

# ����Ĭ�ϲ��� Ĭ�ϲ���ֻ���ڱ���������涨��
def power(x, n = 2) :# Ĭ�Ϸ���ƽ��
    s = 1
    while n > 0 :
        n = n - 1
        s = s * x
    return s
print power(5)

# ����ɱ������ �������һ������������������������Զ���ɱ����
def fn(* args) :
    print args
fn('fds', 89, 'fds')
# ԭ�����Python�Ὣ��Щ������װ��tuple��ֻҪ����Щ��������һ��tuple�Ϳ�����

# ��list������Ƭ
listExample = ['Lisa', 'Bomb', 'Tom', 'Bluse', 'Jerry']
# ȡǰ����Ԫ��
listExample[0:3]

#ֻ��һ��:,��ʾ��ͷ��β
listExample[:]

# ��list����tuple������ȫ��ͬ��ֻ����Ƭ��������tuple

# ������Ƭ
listExample[-2:]
listExample[:-2]
listExample[-4: -1: 2]
#������Ƭ������һ��Ԫ����-1�� ������Ƭ������ʵ��������������������

# ���ַ���������Ƭ
# �ַ������Կ�����һ��list��ÿ��Ԫ�ؾ���һ���ַ�����Ƭ����������ַ���
'ABCDEFG'[:3]
'ABCDEFG'[-3:]
'ABCDEFG'[::2] #'ACEG'

# ���ַ���д
def toUpperFirst(s) :
	return s[0:1].upper() + s[1:]

# ����
# ʹ��forѭ��������list��tuple�����ֱ�����Ϊ����
# Python��forѭ��������������tuple��list���棬���������������κοɵ����Ķ�����
# �����������Ƕ���һ�����ϣ����۸ü���������������������forѭ�����ǿ���ȡ�����ϵ�ÿһ��Ԫ��
# Ŀǰѧϰ�ļ����У� list, tuple, str, unicode(���򼯺�) set(���򼯺�) dict


# ��������
# ��Python�У�������Զ��ȡ��Ԫ�ر�������Ԫ�ص�����
# ʹ��enumerate()������������forѭ����ͬʱ������index��Ԫ��name
# ��ʵ�ϣ�enumerate()��['Adam', 'Lisa', 'Bart', 'Paul']
# ��������ƣ�[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
# ��˵�����ÿһ��Ԫ��ʵ������һ��tuple
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L) :
    print index, '-', name

for t in enumerate(L) :
	index = t[0]
	name = t[1]
	print index, '-', name

# ����dict��value
# dict������һ��values()���������������dictת���ɰ�������value��list
d = {'Adam' : 95, 'Lisa' : 85, 'Bart' : 59}
print d.values()

for v in d.values() :
	print v

# dict ����values()����������һ��itervalues()�������滻values()������Ч��һ��
for v in d.itervalues() :
    print v

# values()����ʵ���ϰ�һ��dictת�����˰���value��list
# inervalues()��������ת���������ڵ����Ĺ��������δ�dict��ȡ��value������inervalues()��������ʡ�ڴ�
# ���һ������˵�Լ����Ե����������Ǿ�ֱ����forѭ��ȥ���������ɼ���������һ�ֳ�������ݲ����������Ե��������ڲ����������κ�Ҫ��

# ����dict��key��value
for key, value in d.items() :
    print key, '-', value
# ��values()��ͬ��items()Ҳ��һ����Ӧ��iteritems()�� iteritems()��ռ�����ڴ�

# �����б�
# Ҫ����list[1,2,3,4,5,6,7,8,9,10], ������range(1,11)
range(1, 11)
# Ҫ����[1x1, 2x2, 3x3,... 10x10]
L = []
for x in range(1, 11) :
    L.append(x * x)
# ʹ��Python�������е��б�����ʽ������������б�
L2 = [x * x for x in range(1, 11)]
# �����ɵ�Ԫ��x*x ����ǰ�棬�������forѭ�����Ϳ��԰�list��������

# ���ӱ��ʽ
# ����ͨ��һ�����ӵ��б�����ʽ��������һ��HTML���
d = {'Adam' : 95, 'Lisa' : 85, 'Bart' : 59}
tds = ['<tr><td>%s</td><td>%s</td></tr>' %(name, score) for name, score in d.iteritems()]
# �ַ�������ͨ��%���и�ʽ������ָ���Ĳ������%s���ַ�����join()�������԰�һ��listƴ�ӳ�һ���ַ���
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

# ��������
[x * x for x in range(1, 11) if x % 2 == 0]

def funUpListStr(l) :
    return [x.upper() for x in l if isinstance(x, str)]

# �����ʽ
[m + n for m in 'ABC' for n in '123']
# �൱��
L = []
for m in 'ABC' :
    for n in '123' :
        L.append(m + n)

# ������������ͬ����λ��
print [str(m) + str(n) + str(o) for m in range(0, 10) for n in range(0, 10) for o in range(0, 10) if m == n and m == o]
print [str(m) + str(n) + str(o) for m in range(0, 10) for n in range(0, 10) for o in range(0, 10) if m == o]
