# -*- coding: cp936 -*-
# ������Ҫ������Python�����һЩ���ⷽ������ʹ��

# Python�����ⷽ��
# ���ⷽ����Python���ֳ�Ϊħ������
# ����Java�е�toString��HashCode����
# ����print [1, 3, 4]ʵ���ϵ��õ���list��__str__()����
print [1, 3, 4].__str__()   # [1, 3, 4]
# ���ӣ�
class Persion(object) :
    def __str__(self) :
        return '<Persion>'
p = Persion()
print p     # <Persion>

# ���ⷽ�����ص㣺
# ������class��
# ����Ҫֱ�ӵ���
# ĳЩ��������������Զ�������Щ����

# Ҫʵ����Щ���ⷽ������ô�й�����һ����Ҫʵ��
# ����ʵ����getattr()�Ļ�����Ҫͬʱȥʵ��setattr(), �Լ�delattr()


# Python������__str__()��__repr__(),ǰ����ʾ�����û��� ���߸�������Ա
# ���ӣ���ʵ�������ַ���
class Persion(object) :
    def __init__(self, name, gender) :
        self.name = name
        self.gender = gender
    def __str__(self) :
        return '<Persion name=%s gender=%s>'%(self.name, self.gender)
    __repr__ = __str__

p = Persion('Tom', 'Male')
print p     # <Persion name=Tom gender=Male>                                                

# __cmp__
# ���������Ҫ�����Լ� ��������������Ļ����͵��ṩ__cmp__()����
class Student(Persion) :
    def __init__(self, name, gender, score) :
        super(Student, self).__init__(name, gender)
        self.score = score
    def __str__(self) :
        return '<Student %s %s $s>'%(self.name, self.gender, self.score)
    __repr__ = __str__

    def __cmp__(self, s) :
        if self.name < s.name :
            return -1
        elif self.name > s.name :
            return 1
        else :
            if self.score > s.score :
                return 1
            elif self.score < s.score :
                return -1
            else :
                return 0

# ������Student��Ϳ���ʵ�ְ�������name����������������ͬ���շ�������
print Student('Tom',  'Male', 89) <  Student('Tom', 'Male', 90) #   True


# __len__
# ���һ������ֵ���һ��list��Ҫ��ȡ�ж��ٸ�Ԫ�أ��͵��õ�len()����
# Ҫ��len()�����������͵��ṩ����__len__()
class Students(object) :
    def __init__(self, * args) :
        self.names = args
    def __len__(self) :
        return len(self.names)

ss = Students('Bob', 'Tom', 'Tim')
print len(ss)   # 3



# ��ѧ����
# ���ӣ�
class Rational(object) :
    def __init__(self, p, q) :
        self.p = p
        self.q = q
    def __add__(self, r) :
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __str__(self) :
        return str(self.p) + " " +str(self.q)
    __repr__ = __str__

r1 = Rational(1, 3)
r2 = Rational(2, 3)
print r1 + r2   # 9 9
# �����ض�����__add__()�Ϳ��Զ���ʹ��+��
# ���໹�� ��
# __sub__��������
# __mul__�˷�����
# __div__��������

# ����ת��
# ���Ҫ��int()������������ʵ��__int__����
# ���������RationalΪ��
class Rational(object) :
    def __init__(self, p, q) :
        self.p = p
        self.q = q
    def __int__(self) :
        return self.p // self.q
# �����Ϳ���ʹ��int������
print int(Rational(4, 2))   # 2
# ͬ��Ҫ��float��������ʵ��__float__()����

# @property
# �����Student�࣬���������Ҫ�޸�һ�����Ե�ʱ�򣬱���score����������
s = Student('Tom', 'Male', 88)
s.score = 99
# ��Ҳ��������д��
s.score = 10000     # ��������Ȼ������˭��ô����������10000��
# ���Դ󲿷ֵ�ʱ�����ǻ���get��set��������������
# ���磺
class Student(object) :
    def __init__(self, name, score) :
        self.name = name
        self.__score = score
    def get_score(self) :
        return self.__score
    def set_score(self, score) :
        if score < 0 or score > 100 :
            raise ValueError('invalid score')
        else :
            self.__score = score
# ����һ����ֻ��ͨ��get��set����������score�����ˣ���score����100��С��0��ʱ��ͻᱨ��
# ����дset��getû��ֱ�ӷ������Է���
# ������ װ������get/set����װ�γ�����������
# ���ӣ�
class Student(object) :
    def __init__(self, name, score) :
        self.name = name
        self.__score = score
    @property
    def score(self) :
        return self.__score
    @score.setter
    def score(self, score) :
        if score < 0 or score > 100 :
            raise ValueError('invalid score')
        else :
            self.__score = score
# ��������һ��score(self)��get��������@propertyװ��
# �ڶ���score(self, score)��set��������@score.setterװ�Ρ�
# @score.setter��ǰһ��@propertyװ�κ�ĸ���Ʒ
# �����Ϳ�����ʹ������һ��������score��
s = Student('Tom', 88)
s.score = 60
print s.score   # 60
# s.score = 1000 �ᱨ��˵�����õ�ȷʵ��score(self, score)����



# __slots__
# ����Python�Ƕ�̬���ԣ����Զ�̬������ԣ��κ�ʵ���������ڶ����Զ�̬�������
# Ҫ��������ӵ����ԣ���������__slots__��ʵ��
# ʹ��__slots__Ҳ���Խ�ʡ�ڴ�
# ���ӣ�
class Student(object) :
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score) :
        self.name = name
        self.gender = gender
        self.score = score
# Student('Alise', 'Meal', 99).address = 'dksssl'
# AttributeError: 'Student' object has no attribute 'address',��������������


# __call__
# ��Python�к�����ʵ��һ������
f = abs
f.__name__
print f(-123) # 123
# ��ˣ� һ����ʵ��Ҳ���Ա��һ���ɵ��ö���
# ֻ��Ҫʵ�����ⷽ��__call__()
# ���ӣ�
class Persion(object) :
    def __init__(self, name, gender) :
        self.name = name
        self.gender = gender
    def __call__(self, firend) :
         print 'My name is %s...' %self.name
         print 'My firend is %s...' % firend
p = Persion('Tom', 'Male')
p('Bob')    # ���԰�һ�����󵱳�һ��������ʹ��,��Ϊʵ����__call__()����
# My name is Tom...
# My firend is Bob...
# ����p('Bob')�޷��ֱ�����ʵ�����Ǻ����������Python�к���Ҳ�Ƕ��󣬶���ͺ��������𲢲�����































