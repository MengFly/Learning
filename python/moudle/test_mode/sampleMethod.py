# -*- coding: cp936 -*-
# 这里主要介绍了Python里面的一些特殊方法及其使用

# Python的特殊方法
# 特殊方法在Python中又称为魔术方法
# 很像Java中的toString，HashCode方法
# 比如print [1, 3, 4]实际上调用的是list的__str__()方法
print [1, 3, 4].__str__()   # [1, 3, 4]
# 例子：
class Persion(object) :
    def __str__(self) :
        return '<Persion>'
p = Persion()
print p     # <Persion>

# 特殊方法的特点：
# 定义在class中
# 不需要直接调用
# 某些函数或操作符会自动调用这些方法

# 要实现这些特殊方法，那么有关联的一定都要实现
# 例如实现了getattr()的话，就要同时去实现setattr(), 以及delattr()


# Python定义了__str__()和__repr__(),前者显示给给用户， 后者给开发人员
# 例子，简单实现这两种方法
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
# 如果我们想要我们自己 定义的类可以排序的话，就得提供__cmp__()函数
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

# 上述的Student类就可以实现按照姓名name来进行排序，姓名相同按照分数排序
print Student('Tom',  'Male', 89) <  Student('Tom', 'Male', 90) #   True


# __len__
# 如果一个类表现的像一个list。要获取有多少个元素，就得用到len()函数
# 要让len()正常工作，就得提供方法__len__()
class Students(object) :
    def __init__(self, * args) :
        self.names = args
    def __len__(self) :
        return len(self.names)

ss = Students('Bob', 'Tom', 'Tim')
print len(ss)   # 3



# 数学运算
# 例子：
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
# 在类重定义了__add__()就可以对类使用+了
# 其余还有 ：
# __sub__减法运算
# __mul__乘法运算
# __div__除法运算

# 类型转换
# 如果要让int()正常工作，得实现__int__方法
# 以上面的类Rational为例
class Rational(object) :
    def __init__(self, p, q) :
        self.p = p
        self.q = q
    def __int__(self) :
        return self.p // self.q
# 这样就可以使用int方法了
print int(Rational(4, 2))   # 2
# 同理，要让float工作，得实现__float__()方法

# @property
# 上面的Student类，如果我们想要修改一个属性的时候，比如score，可以这样
s = Student('Tom', 'Male', 88)
s.score = 99
# 但也可以这样写：
s.score = 10000     # 但这样显然不合理，谁这么吊分数会有10000分
# 所以大部分的时候我们会用get和set方法来进行设置
# 例如：
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
# 这样一来就只能通过get和set方法来设置score属性了，当score大于100或小于0的时候就会报错
# 但是写set和get没有直接访问属性方便
# 可以用 装饰器把get/set方法装饰成属性来调用
# 例子：
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
# 这样，第一个score(self)是get方法，用@property装饰
# 第二个score(self, score)是set方法，用@score.setter装饰。
# @score.setter是前一个@property装饰后的副产品
# 这样就可以像使用属性一样来设置score了
s = Student('Tom', 88)
s.score = 60
print s.score   # 60
# s.score = 1000 会报错，说明调用的确实是score(self, score)方法



# __slots__
# 由于Python是动态语言，可以动态添加属性，任何实例在运行期都可以动态添加属性
# 要想限制添加的属性，可以利用__slots__来实现
# 使用__slots__也可以节省内存
# 例子：
class Student(object) :
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score) :
        self.name = name
        self.gender = gender
        self.score = score
# Student('Alise', 'Meal', 99).address = 'dksssl'
# AttributeError: 'Student' object has no attribute 'address',不能添加这个属性


# __call__
# 在Python中函数其实是一个对象
f = abs
f.__name__
print f(-123) # 123
# 因此， 一个类实例也可以变成一个可调用对象
# 只需要实现特殊方法__call__()
# 例子：
class Persion(object) :
    def __init__(self, name, gender) :
        self.name = name
        self.gender = gender
    def __call__(self, firend) :
         print 'My name is %s...' %self.name
         print 'My firend is %s...' % firend
p = Persion('Tom', 'Male')
p('Bob')    # 可以把一个对象当成一个函数来使用,因为实现了__call__()方法
# My name is Tom...
# My firend is Bob...
# 但看p('Bob')无法分别它是实例还是函数，因此在Python中函数也是对象，对象和函数的区别并不显著































