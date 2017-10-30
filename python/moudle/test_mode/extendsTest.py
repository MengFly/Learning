# -*- coding: cp936 -*-
# �̳�
# ����Ѿ�������Persion�ࡣ��Ҫ�����µ�Student��Teacher��ʱ������ֱ�Ӵ�Persion��̳�
class Persion(object):  # �����е�object��ʾPersion���object���м̳�
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# ����Student��ʱ,ֻ��Ҫ�Ѷ�������Լ��ϣ�����score
class Student(Persion):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


# һ��Ҫ��super(Student, self).__init__(name, gender)ȥ��ʼ�����࣬����̳���Persion��Student��û��name��gender
# ����super(Student, self)�����ص�ǰ��̳еĸ��࣬��Persion��Ȼ�����__init__()����
# self�����Ѿ���super�д�����__init__()�н���ʽ���ݣ�����д��


# �ж�����
# ����isinstance()�����ж�һ������������
# �ٶ���һ��Teacher�࣬�̳���Persion��
class Teacher(Persion):
    def __init__(self, name, gender, coutse):
        super(Teacher, self).__init__(name, gender)
        self.coutse = coutse


p = Persion('Tom', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Famale', 'English')
print(isinstance(p, Persion))  # True
print(isinstance(t, Persion))  # True
print(isinstance(p, Student))  # False
print(isinstance(t, Student))  # False
# �����˵��������Կ����Ǹ�������ͣ������಻������������ͣ��ͺ���ѧ����һ���ˣ����˲�һ����ѧ��һ��

# isinstanceҲ����������
print(isinstance(78, int))  # True
print(isinstance('Tom', str))  # True
print(isinstance([8, 8], list))  # True
print(isinstance((8, 8), tuple))  # True
print(isinstance({3: 3, 'Tom': 3}, dict))  # True


# ��̬
# ����м̳й�ϵ�������������Ϳ�������ת�Ϳ�����������ͣ�������Ǵ�Persion������Student��Teacher������д��whoAmI()����
class Persion(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return 'I am a persion, My name is %s' % self.name


class Student(Persion):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def whoAmI(self):
        return 'I am a Student, My name is %s' % self.name


class Teacher(Persion):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

    def whoAmI(self):
        return 'I am a Teacher, My name is %s' % self.name


# �����Ļ�����һ���������������һ������x,����x��Persion����Student�Լ�Teacher����������ȷ��ӡ
def who_am_i(x):
    print
    x.whoAmI()


p = Persion('Tom', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')
who_am_i(p)  # I am a persion, My name is Tom
who_am_i(s)  # I am a Student, My name is Bob
who_am_i(t)  # I am a Teacher, My name is Alice


# ����Python�Ƕ�̬���ԣ�Ҳ����Դ�������ͽ��м�飬��˶�̬���ֵĲ�����Java��ô���ԣ�ֻҪ�����д���whoAmI()�������࣬ʵ���϶����Դ����������


# ���ؼ̳�
# ��Java��ͬ��Python����Ӷ������̳�
# ���磺
class A(object):
    def __init__(self, a):
        print
        'A init----'
        self.a = a


class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print
        'B init----'


class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print('C init----')


class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print('D init----')


d = D('a')
# A init----
# C init----
# B init----
# D init----
# ��ȻA���̳������Σ���__init__()ֻ����һ��

# ��ȡ������Ϣ
# ����ʹ��type()������ȡ����������
s = Student('Tom', 'Male', 88)
print(type(s))  # <class '__main__.Student'>
# ����ʹ��dir()������ȡ��������������
print(dir(s))
# ['__class__', '__delattr__', '__dict__', '__doc__',
# '__format__', '__getattribute__', '__hash__', '__init__',
# '__module__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'gender', 'name', 'score', 'whoAmI']

# dir()���ص��������ַ����б������֪һ���������ƣ�Ҫ��ȡ�������ö�������ԣ�����Ҫ��getattr()��setattr()������
print(getattr(s, 'name'))  # Tom
setattr(s, 'name', 'Adam')
print(s.name)  # Adam
# ���Ҫ��ȡ�����ڵ����ԣ��ͻᱨ��
# ����getattr(s, 'age')  
# �������Ĭ��ֵ���Ͳ��ᱨ�������Բ����ڵ�ʱ��ͷ���Ĭ��ֵ
print(getattr(s, 'age', 20))  # 20
