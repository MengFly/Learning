# -*- coding: cp936 -*-
# 面向对象编程
# 类用于定义抽象类型
# 实例根据类的定义被创建出来（不会的去学Java）
# 用关键字class 来创建类
# 实例-- 例如：xiaomimg = Presion() xiaojun = Persion()
# 定义一个类:
class Persion() :       # Python 中类名大写
    pass
xiaoming = Persion()
print xiaoming

# 创建实例属性
# 创建好实例后，可以直接给实例的属性赋值，但这个属性不一定在类中声明
# 例如 ：
xiaohong = Persion()
xiaohong.name = 'xiaohong'
xiaohong.grade = 2
xiaohong.grade = xiaohong.grade + 1
print xiaohong.name, xiaohong.grade # xiaohong 3


# 初始化实例属性
# 在定义类的时候，可以为类定义一个__init__()方法，用于对类进行初始化。当创建实例的时候，__init__()方法就会自动调用
# __init__()的第一个参数必须为self
# 例子：
class Persion() :
    def __init__(self, name, gender, birth) :
        self.name = name
        self.gender = gender
        self.birth = birth
        print '__init()__ call... self.name=%s self.gender=%s self.birth=%s'%(self.name, self.gender, self.birth)
# 创建实例的时候要提供self之外的所有参数
# 例如：
xiaomei = Persion('xiaomei', 4, '09-08-07') #__init()__ call... self.name=xiaomei self.gender=4 self.birth=09-08-07
# 从打印结果来看，__init__()确实被自动调用了


# 访问限制
# 如果一个属性是以双下划线'__'开头，那么这个属性就无法被外部访问
# 例子：
class Persion() :
    def __init__(self, name) :
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'
p = Persion('Bob')
print p.name    # Bob
print p._title  # Mr
# 而当访问p.__job的时候就会出错
# 如果一个属性以__xxx__的形式定义，那么他就又可以被外部访问了
# 以__xxx__定义的的属性在Python的类中被称为特殊属性
# 通常我们不把普通属性用__xxx__定义
# 以单下划线开头的属性，_xxx虽然也可以被外部访问，但按照习惯，他们不应该被外部访问


# 创建类属性
# 如果在类上绑定一些属性，而不是在实例上绑定，那么所有的实例都可以访问类的属性，  并且所有实例访问的类属性都是同一个
# 实例属性每个实例各自拥有，互相独立，而类属性有且只有一份
# 定义雷属性可以直接在class 中定义
# 例子：
class Persion() :
    address = 'Earth'
    def __init__(self, name) :
        self.name = name
# 访问类属性不需要实例。直接使用类即可
print Persion.address   # Earth
# 所有的实例也是可以访问类属性的
p1 = Persion('Tom')
p2 = Persion('Jerry')
print p1.address    # Earth
print p2.address    # Earth
# 雷属性可以修改：
Persion.address = 'China'
print p1.address    # China
print p2.address    # China


# 在访问属性的时候，实例属性优先级高于类属性（即如果实例属性和类属性重名，优先访问实例属性）
# 例子：
Persion.address = 'Earth'
p1.address = 'China'    # 在这里的时候，给p1创建了一个address的实例变量
print p1.address    # China 这个时候访问的是p1 的实例变量
print Persion.address   # Earth
# 因此，千万不要在实例上面修改类属性，它实际上没有修改类属性，而是给实例绑定了一个实例属性

# 定义实例方法
# 实例方法的第一个参数必须是self，指向调用该方法的实例本身
# 对于外部没法访问的__xxx类的属性，类的实例方法可以调用
# 例子：
class Persion() :
    def __init__(self, name) :
        self.__name = name

    def get_name(self) :
        return self.__name
p = Persion('Bob')
print p.get_name()  #Bob


# 在类中定义的实例方法其实也是属性，它实际上是一个函数对象
# 例如上面的:
print p.get_name    #<bound method Persion.get_name of <__main__.Persion instance at 0x02ED2DF0>>
method1 = p.get_name
print method1() # 'Bob'
# 因此可见实例方法也是属性，可以以属性的方式来访问

# 因为方法也是一个属性，所以，他也可以动态地添加到实例上，只是需要用type.MethodType()把一个函数变为一个方法
# 例子：
import types
def fn_grade(self) :
    if self.score >= 80 :
        return 'A'
    if self.score >= 60 :
        return 'B'
    return 'C'
class Persion() :
    def __init__(self, name, score) :
        self.name = name
        self.score = score
p1 = Persion('Bob', 90)
p1.get_grade = types.MethodType(fn_grade, p1, Persion)
print p1.get_grade()    # A
# 这样就给实例添加上方法了
#可是如果再新建一个实例，它里面是没有这个方法的
# p2 = Persion('Tom', 89) p2.get_grade()    #Error Persion instance has no attribute 'get_grade'
# 给一个实例动态添加方法并不常见，直接在class中定义更为直观


# 定义类方法
# 通过标记一个@classmethod，那么该方法就会绑定到class上面，而不是类的实例。
# 例子：
class Persion() :
    count = 0
    @classmethod
    def how_many(cls) :
        return cls.count
    def __init__(self, name) :
        self.name = name
        Persion.count = Persion.count + 1
print Persion.how_many()    #0
p1 = Persion('Bob')
print Persion.how_many()    #1





























        

