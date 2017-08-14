# -*- coding: cp936 -*-
# װ����

# ����������
# LEGB �� L > E > G > B
# L : local �����ڲ�������
# E : enclosing �����ڲ�����Ƕ����֮��
# G : global ȫ��������
# B : build-in ����������
# Ҳ��������������в���

# Python�հ�
# �հ��ĸ��
# �ڲ������ж�enclosing������ı�����������
# ���ӣ�
def func(var) :
    def in_func() :
        return var
    return in_func
f = func(89)
print f     # <function in_func at 0x03081AF0>
print f()   # 89

# ���ñհ����ǾͿ��Եõ��ж�ʱ�򼰸������Ϊ100��150����������ĺ���
# ��������Ҳ�Ͳ���ȥר�ű�д����������
def set_passline(passline) :
    def cmp(val) :
        if val >= passline :
            print '�㼰���ˣ�����Ϊ�� %d'%val
        else :
            print '��û�м���'
    return cmp
func_100 = set_passline(60) # �ж�����Ϊ100���Ƿ񼰸�
func_150 = set_passline(90) # �ж�����Ϊ150���Ƿ񼰸�

# ���ú���
func_100(59)    # ��û�м���
func_100(60)    # �㼰���ˣ�����Ϊ�� 60
func_150(90)    # �㼰���ˣ�����Ϊ�� 90
func_150(60)    # ��û�м���
# Ҳ����˵�հ������þ���ͨ���ڲ����������ⲿ������enclosing�������ֵ�Ӷ�ʵ�ֲ�ͬ���ܵĺ���
# ͨ����������ڲ��������ǾͿ��Եõ�������Ҫ�ĺ���
# ����Ҳ�ͼ����˴������д

# ������������������ͺ���ƽ�����ĺ�����
def my_sum(* args) :
    return sum(args)
def my_average(* args) :
    return sum(args) / len(args)
# ��������ĺ����������ƣ���Ϊ��û�в�����������ַ�����ʱ��ͻᱨ���޸����£�
def my_sum(* args) :
    if len(args) == 0 :
        return 0    # �����������ʱ�򷵻�0
    for arg in args :
        if not isinstance(arg, int) :
            return 0    # ����в�������������Ҳ����0
    return sum(args) 
def my_average(* args) :
    if len(args) == 0 :
        return 0    # �����������ʱ�򷵻�0
    for arg in args :
        if not isinstance(arg, int) :
            return 0    # ����в�������������Ҳ����0
    return sum(args) / len(args)
# ���Կ����������δ��������кܶ����ظ���
# ���ñհ������ǾͿ��԰�������ͬ���߼��������
# ���ӣ�
def dec(func)  :    # ����Ĳ�����һ������
    def in_dec(* args) :
        if len(args) == 0 :
            return 0    # �����������ʱ�򷵻�0
        for arg in args :
            if not isinstance(arg, int) :
                return 0    # ����в�������������Ҳ����0
        return func(* args)
    return in_dec
# �����dec�������൱�ڸ�dec����ĺ������������ƣ�������func�����������ж�
# ���õ�ʱ��Ϳ���������
def my_sum(* args) :
    return sum(args)
def my_average(* ages) :
    return sum(args)/ len(args)
my_sum = dec(my_sum)
my_average = dec(my_average)
print my_sum()
print my_average()
# ʵ����my_sum��my_averageʵ���Ͼ���dec���������in_dec�������磺
print my_sum.__name__   # in_dec
# �����Ϳ��Զ�̬Ϊ��������¹�����

# Python װ����
# װ��������װ�κ���
# ����һ����������
# ��װ�κ�����ʶ��ָ�򷵻صĺ�������
# װ����ʵ���Ͼ��Ǽ򻯴������д
# ��������Ĵ���дһ��װ���������ӣ�
def dec(func)  :    # ����Ĳ�����һ������
    print 'dec call....'
    def in_dec(* args) :
        print 'in_dec call....'
        if len(args) == 0 :
            return 0    # �����������ʱ�򷵻�0
        for arg in args :
            if not isinstance(arg, int) :
                return 0    # ����в�������������Ҳ����0
        return func(* args)
    return in_dec
# ����ĺ�������˼��д�ӡ��䡣��֤��������ִ��
# ����ʹ��װ����
@ dec
def my_sum(* args) :
    return sum(args)
# ִ���������䣬�ͻ����һ�䣺dec call....
# ˵��dec������ִ����
# ��������ִ��һ��my_sum()����
print my_sum(), my_sum.__name__ # in_dec call.... 0 in_dec
# ˵��my_sum()ʵ�����Ѿ������in_dec()����
# ʹ��װ�������Ǽ�ǰ��һ�����ӵĴ���
# ʵ���Ͼ��൱��my_sum = dec(my_sum)





























