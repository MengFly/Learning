# -*- coding: cp936 -*-
# if���, Python�����Ĺ����ĸ��ո񣬶�����ʹ��Tab��
age = 20
if age >= 18 :
    print "adult", age
print "END"
# �˳�����Ҫ�ఴһ�пո�
if not age >= 18 :
    print 'child age is', age

# if-else
if age >= 18 :
    print "adult age is", age
else :
    print "child age is", age

# Ƕ�׵�if-else
if age >= 18 :
    print 'adult'
else :
    if age >= 3 :
        print 'kid'
    else :
        print 'baby'

# if - elif
if age >= 20 :
	print 'adult'
elif age >= 12 :
	print 'child'
elif age >= 3 :
	print 'kid'
else :
	print 'baby'

	
# for ѭ������list�е�Ԫ��
listExample = ["I", "Love", "��", "�h", "��"]
for name in listExample :
    print name


# while
N = 10
x = 0
while x < N :
    print x
    x = x + 1

# break
x = 0
while x < N :
    print x
    if x >= 5 :
        break
    x = x + 1

# continue
l = [23,65,76,34,76,87,56,98,76]
for score in l :
	if score < 60 :
		continue
	else :
		print "������, ����Ϊ ��", score


# ����ѭ��
for name in ['Tom', 'Bob', 'Jerry'] :
    for score in ['87', '88', '89'] :
        print name + score

# dict dict ���൱��Java�����map
# ����dict�����ж��ٸ�Ԫ�أ����ҵ��ٶȶ���һ����
# ȱ���� ռ���ڴ�󣬻��˷Ѻܶ�����
# dict�������
d = {
	'Adam' : 98,
	'Bob' : 77,
	'Jerry' : 87
	}
print d

# len�������Լ������⼯�ϵĳ���
len(d)

# ����dict
print d['Adam']

# ���key���ڣ���᷵��value�������������ᱨ��keyError

# �ж�key�Ƿ����
if 'Adam' in d :
    print d['Adam']

# ʹ��get���������key���ڷ���value����������ڷ���None

print d.get('Bob')
print d.get('Je')

# dict��keyԪ�ض��ǲ��ɱ�ģ�python�Ļ������ͣ��ַ��������������������ǲ��ɱ�ģ���������Ϊkey����list�ǿɱ�ģ����Բ�����Ϊkey
d2 = {
    ('3', '3') : 'fdss'
    }
d2.get(('3', '3'))

# ����dict
# ����µ�Ԫ�أ�ʹ��û����ӹ���key��value
d2['��������ӵ�key'] = '��������ӵ�ֵ'

print d2
# ���key�Ѿ����ڣ���ͻ���º�key��ص�value
d2['��������ӵ�key'] = '֮ǰ��ֵ�Ѿ������滻��'
print d2

# ����dict
for key in d2 :
    print key, '=>', d2[key]

# set set����һϵ��Ԫ�أ���һ���list���񣬵�setԪ�ز����ظ�������������ģ���һ���dict����
# ����set
s = set(['A', 'B', 'C'])

# ����set, ͬ��������ʹ��forѭ������list����������set
# �ж�Ԫ���Ƿ���set��
print 'A' in s

# �ɱ���󲻿��Է���set��
weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
x = 'WED'
if x in weekdays :
    print 'input ok'
else :
    print 'input error'

# ����set(���Ԫ��add()��ɾ��Ԫ��remove())
myset = set(['I', 'Love', '��', '�h', '��'])
myset.add(0)
myset.remove(0)









