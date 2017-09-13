# list
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

for item in shoplist:
             print(item, end=" ")

shoplist.append('rice')
print('My shopping list is now ', shoplist)
shoplist.sort()
print('My shopping sort list is now ', shoplist)

olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)


# 元组
#元组和字符串一样是不可变的即你不能修改元组
zoo = ('python', 'elephant', 'penguin')
newzoo = ('monkey', 'camel', zoo)
print('newzoo is', newzoo)
print('Last animal brought from old zoo is', newzoo[2][2])
#单个元素的元组就不那么简单了。你必须在第一个（唯一一个）项目后跟一个逗号，这样 Python 才能区分元组和表达式中一个带圆括号的对象
oneitem = (2,)
print(len(oneitem))


# 字典
#记住字典中的键/值对是没有顺序的。如果你想要一个特定的顺序，那么你应该在使用前自己对它们排序
ab= { 'swaroop' : 'swaroop@swaroopch.com',
                          'Larry' : 'larry@wall.org',
                          'Matsumoto' : 'matz@ruby-lang.org',
                          'Spammer' : 'spammer@hotmail.com'
      }
print('Swaroop\'s address is', ab['swaroop'])
del ab['Spammer']
print('There are {} contacts in the address-book'.format(len(ab)))
for name, address in ab.items():
             print('Contact {} at {} '.format(name, address))
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
             print("\nGuido's address is", ab['Guido'])


# 切片
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
print('shoplist is', shoplist)
print('name[0] is', name[0])
print('item 1 to 3 is',  shoplist[1:3])
print('item 2 to end is', shoplist[2:])
print('item 1 to -1 is', shoplist[1 :-1])
print('item start to end is', shoplist[:])

print('切片的第三个参数是切片的步长')
print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::3])
print(shoplist[::-1])


# 集合
bri = set(['brazil', 'russla', 'india'])
print('india' in bri)
print('usa' in bri)
bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))
bri.remove('russla')
print(bri & bric)

#如果你想要复制一个列表
#或者类似的序列或者其他复杂的对象（不是如整数那样的简单对象），那么你必须使用切片操作符来取得拷贝
simplearr = [2, 3, 4,5]
copyarr = simplearr[:]
copyarr2 = simplearr.copy()
print('simplearr :', simplearr)
print('copyarr     :', copyarr)
print('copyarr2 :', copyarr2)


# 字符串
name = 'Swaroop'
if name.startswith('Swa'):
             print('Yes, This string starts with "Swa"')
if 'a' in name:
             print('Yes, This string contains the string "a"')
if name.find('war') != -1:
             print('Yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))















