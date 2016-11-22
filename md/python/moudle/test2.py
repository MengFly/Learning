# -*- coding: cp936 -*-
# if语句, Python缩进的规则，四个空格，而不是使用Tab键
age = 20
if age >= 18 :
    print "adult", age
print "END"
# 退出缩进要多按一行空格
if not age >= 18 :
    print 'child age is', age

# if-else
if age >= 18 :
    print "adult age is", age
else :
    print "child age is", age

# 嵌套的if-else
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

	
# for 循环遍历list中的元素
listExample = ["I", "Love", "潘", "玥", "利"]
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
		print "及格了, 分数为 ：", score


# 多重循环
for name in ['Tom', 'Bob', 'Jerry'] :
    for score in ['87', '88', '89'] :
        print name + score

# dict dict 就相当于Java里面的map
# 无论dict里面有多少个元素，查找的速度都是一样的
# 缺点是 占用内存大，会浪费很多内容
# dict是无序的
d = {
	'Adam' : 98,
	'Bob' : 77,
	'Jerry' : 87
	}
print d

# len函数可以计算任意集合的长度
len(d)

# 访问dict
print d['Adam']

# 如果key存在，则会返回value。如果不存在则会报错keyError

# 判断key是否存在
if 'Adam' in d :
    print d['Adam']

# 使用get方法，如果key存在返回value。如果不存在返回None

print d.get('Bob')
print d.get('Je')

# dict的key元素都是不可变的，python的基本类型，字符串，整数，浮点数都是不可变的，都可以作为key，但list是可变的，所以不能作为key
d2 = {
    ('3', '3') : 'fdss'
    }
d2.get(('3', '3'))

# 更新dict
# 添加新的元素：使用没有添加过的key和value
d2['我是新添加的key'] = '我是新添加的值'

print d2
# 如果key已经存在，则就会更新和key相关的value
d2['我是新添加的key'] = '之前的值已经被我替换了'
print d2

# 遍历dict
for key in d2 :
    print key, '=>', d2[key]

# set set持有一系列元素，这一点和list很像，但set元素不能重复，而且是无序的，这一点和dict很像
# 创建set
s = set(['A', 'B', 'C'])

# 访问set, 同样可以像使用for循环遍历list那样来遍历set
# 判断元素是否在set中
print 'A' in s

# 可变对象不可以放在set中
weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
x = 'WED'
if x in weekdays :
    print 'input ok'
else :
    print 'input error'

# 更新set(添加元素add()，删除元素remove())
myset = set(['I', 'Love', '潘', '玥', '利'])
myset.add(0)
myset.remove(0)









