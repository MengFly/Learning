# -*- coding: cp936 -*-
# ���������
# �����ڶ����������
# ʵ��������Ķ��屻���������������ȥѧJava��
# �ùؼ���class ��������
# ʵ��-- ���磺xiaomimg = Presion() xiaojun = Persion()
# ����һ����:
class Persion() :       # Python ��������д
    pass
xiaoming = Persion()
print xiaoming

# ����ʵ������
# ������ʵ���󣬿���ֱ�Ӹ�ʵ�������Ը�ֵ����������Բ�һ������������
# ���� ��
xiaohong = Persion()
xiaohong.name = 'xiaohong'
xiaohong.grade = 2
xiaohong.grade = xiaohong.grade + 1
print xiaohong.name, xiaohong.grade # xiaohong 3


# ��ʼ��ʵ������
# �ڶ������ʱ�򣬿���Ϊ�ඨ��һ��__init__()���������ڶ�����г�ʼ����������ʵ����ʱ��__init__()�����ͻ��Զ�����
# __init__()�ĵ�һ����������Ϊself
# ���ӣ�
class Persion() :
    def __init__(self, name, gender, birth) :
        self.name = name
        self.gender = gender
        self.birth = birth
        print '__init()__ call... self.name=%s self.gender=%s self.birth=%s'%(self.name, self.gender, self.birth)
# ����ʵ����ʱ��Ҫ�ṩself֮������в���
# ���磺
xiaomei = Persion('xiaomei', 4, '09-08-07') #__init()__ call... self.name=xiaomei self.gender=4 self.birth=09-08-07
# �Ӵ�ӡ���������__init__()ȷʵ���Զ�������


# ��������
# ���һ����������˫�»���'__'��ͷ����ô������Ծ��޷����ⲿ����
# ���ӣ�
class Persion() :
    def __init__(self, name) :
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'
p = Persion('Bob')
print p.name    # Bob
print p._title  # Mr
# ��������p.__job��ʱ��ͻ����
# ���һ��������__xxx__����ʽ���壬��ô�����ֿ��Ա��ⲿ������
# ��__xxx__����ĵ�������Python�����б���Ϊ��������
# ͨ�����ǲ�����ͨ������__xxx__����
# �Ե��»��߿�ͷ�����ԣ�_xxx��ȻҲ���Ա��ⲿ���ʣ�������ϰ�ߣ����ǲ�Ӧ�ñ��ⲿ����


# ����������
# ��������ϰ�һЩ���ԣ���������ʵ���ϰ󶨣���ô���е�ʵ�������Է���������ԣ�  ��������ʵ�����ʵ������Զ���ͬһ��
# ʵ������ÿ��ʵ������ӵ�У����������������������ֻ��һ��
# ���������Կ���ֱ����class �ж���
# ���ӣ�
class Persion() :
    address = 'Earth'
    def __init__(self, name) :
        self.name = name
# ���������Բ���Ҫʵ����ֱ��ʹ���༴��
print Persion.address   # Earth
# ���е�ʵ��Ҳ�ǿ��Է��������Ե�
p1 = Persion('Tom')
p2 = Persion('Jerry')
print p1.address    # Earth
print p2.address    # Earth
# �����Կ����޸ģ�
Persion.address = 'China'
print p1.address    # China
print p2.address    # China


# �ڷ������Ե�ʱ��ʵ���������ȼ����������ԣ������ʵ�����Ժ����������������ȷ���ʵ�����ԣ�
# ���ӣ�
Persion.address = 'Earth'
p1.address = 'China'    # �������ʱ�򣬸�p1������һ��address��ʵ������
print p1.address    # China ���ʱ����ʵ���p1 ��ʵ������
print Persion.address   # Earth
# ��ˣ�ǧ��Ҫ��ʵ�������޸������ԣ���ʵ����û���޸������ԣ����Ǹ�ʵ������һ��ʵ������

# ����ʵ������
# ʵ�������ĵ�һ������������self��ָ����ø÷�����ʵ������
# �����ⲿû�����ʵ�__xxx������ԣ����ʵ���������Ե���
# ���ӣ�
class Persion() :
    def __init__(self, name) :
        self.__name = name

    def get_name(self) :
        return self.__name
p = Persion('Bob')
print p.get_name()  #Bob


# �����ж����ʵ��������ʵҲ�����ԣ���ʵ������һ����������
# ���������:
print p.get_name    #<bound method Persion.get_name of <__main__.Persion instance at 0x02ED2DF0>>
method1 = p.get_name
print method1() # 'Bob'
# ��˿ɼ�ʵ������Ҳ�����ԣ����������Եķ�ʽ������

# ��Ϊ����Ҳ��һ�����ԣ����ԣ���Ҳ���Զ�̬����ӵ�ʵ���ϣ�ֻ����Ҫ��type.MethodType()��һ��������Ϊһ������
# ���ӣ�
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
# �����͸�ʵ������Ϸ�����
#����������½�һ��ʵ������������û�����������
# p2 = Persion('Tom', 89) p2.get_grade()    #Error Persion instance has no attribute 'get_grade'
# ��һ��ʵ����̬��ӷ�������������ֱ����class�ж����Ϊֱ��


# �����෽��
# ͨ�����һ��@classmethod����ô�÷����ͻ�󶨵�class���棬���������ʵ����
# ���ӣ�
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





























        

