# self
#类的方法与普通的函数只有一个特别的区别 —— 它们必须有一个额外的第一个参数名称，但是在调用这个方法的时候你不为这个参数赋值


# 类
class Person:
             def __init__(self, name):
                          self.name = name
             def sayHi(self):
                          print('hello, My Name is {}, how are you?'.format(self.name))

p = Person('Swaroop')
print(p)
p.sayHi()


# 类和对象变量
class Robot:
             ''' Represents a robot , with a name'''
             # a class variable, counting the number of robots
             population = 0

             def __init__(self, name):
                          '''Initializes the data.'''
                          self.name = name
                          print('(initalize {})'.format(self.name))
                          #When this person is created, the robot adds to the population
                          Robot.population += 1

             def __del__(self):
                          '''I am dying.'''
                          print('{0} is being destroyed!'.format(self.name))
                          Robot.population -= 1
                          if Robot.population == 0:
                                       print('{0} was the last one.'.format(self.name))
                          else:
                                       print("There are still {0:d} robots working.".format(Robot.population))

             def sayHi(self):
                          print('Greetings , my master call me {0}.'.format(self.name))

             def howMany():
                          print('We have {0:d} robots.'.format(Robot.population))
             howMany = staticmethod(howMany)

             @staticmethod
             def wecando():
                          print(help(Robot))
             
droid1 = Robot("R2-D2")
droid1.sayHi()
Robot.howMany()

droid2 = Robot("C-3P0")
droid2.sayHi()
Robot.howMany()

print('now delete robot...')
del droid1
del droid2
Robot.howMany()
Robot.wecando()


# 继承
class SchoolMember:
             def __init__(self, name, age):
                          self.name = name
                          self.age = age
                          print('(Initialize SchoolMember:{0})'.format(self.name))

             def tell(self):
                          print('Name : {0}   Age : {1}'.format(self.name, self.age), end="   ")

class Teacher(SchoolMember):
             def __init__(self, name, age, salary):
                          SchoolMember.__init__(self, name, age)
                          self.salary = salary
                          print('(Initialized Teacher:{0})'.format(self.name))

             def tell(self):
                          SchoolMember.tell(self)
                          print('Salary:"{0:d}"'.format(self.salary))

class Student(SchoolMember):
             def __init__(self, name, age, marks):
                          SchoolMember.__init__(self, name, age)
                          self.marks = marks
                          print('(Initialized Student:{0})'.format(self.name))

             def tell(self):
                          SchoolMember.tell(self)
                          print('Marks:"{0:d}"'.format(self.marks))


t = Teacher("Mrs.Shrvidya", 30, 30000)
s = Student("Swaroop", 25, 75)
print()

members = [t, s]
for member in members:
             member.tell()


























