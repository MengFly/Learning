# -*- coding: cp936 -*-
# 继承
# 如果已经定义了Persion类。需要定义新的Student和Teacher类时。可以直接从Persion类继承
class Persion(object):  # 括号中的object表示Persion类从object类中继承
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 定义Student类时,只需要把额外的属性加上，例如score
class Student(Persion):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


# 一定要用super(Student, self).__init__(name, gender)去初始化父类，否则继承自Persion的Student将没有name和gender
# 函数super(Student, self)将返回当前类继承的父类，即Persion，然后调用__init__()方法
# self参数已经在super中传入在__init__()中将隐式传递，不能写出


# 判断类型
# 函数isinstance()可以判断一个变量的类型
# 再定义一个Teacher类，继承自Persion类
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
# 上面的说明子类可以看做是父类的类型，而父类不能是子类的类型，就好像学生是一个人，而人不一定是学生一样

# isinstance也可以这样用
print(isinstance(78, int))  # True
print(isinstance('Tom', str))  # True
print(isinstance([8, 8], list))  # True
print(isinstance((8, 8), tuple))  # True
print(isinstance({3: 3, 'Tom': 3}, dict))  # True


# 多态
# 类具有继承关系，并且子类类型可以向上转型看做父类的类型，如果我们从Persion派生出Student和Teacher，并都写了whoAmI()方法
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


# 这样的话，在一个函数中如果接受一个变量x,无论x是Persion还是Student以及Teacher，都可以正确打印
def who_am_i(x):
    print
    x.whoAmI()


p = Persion('Tom', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')
who_am_i(p)  # I am a persion, My name is Tom
who_am_i(s)  # I am a Student, My name is Bob
who_am_i(t)  # I am a Teacher, My name is Alice


# 由于Python是动态语言，也不会对传入的类型进行检查，因此多态表现的并不像Java那么明显，只要是类中存在whoAmI()方法的类，实际上都可以传入这个方法


# 多重继承
# 于Java不同，Python允许从多个父类继承
# 例如：
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
# 虽然A被继承了两次，但__init__()只调用一次

# 获取对象信息
# 可以使用type()函数获取变量的类型
s = Student('Tom', 'Male', 88)
print(type(s))  # <class '__main__.Student'>
# 可以使用dir()函数获取变量的所有属性
print(dir(s))
# ['__class__', '__delattr__', '__dict__', '__doc__',
# '__format__', '__getattribute__', '__hash__', '__init__',
# '__module__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'gender', 'name', 'score', 'whoAmI']

# dir()返回的属性是字符串列表，如果已知一个属性名称，要获取或者设置对象的属性，就需要用getattr()和setattr()函数了
print(getattr(s, 'name'))  # Tom
setattr(s, 'name', 'Adam')
print(s.name)  # Adam
# 如果要获取不存在的属性，就会报错
# 例如getattr(s, 'age')  
# 如果设置默认值，就不会报错，当属性不存在的时候就返回默认值
print(getattr(s, 'age', 20))  # 20
