$sim                                                        ''

Dim x as integer : x = 8
Dim y as integer : y = 678
Dim z as byte

print "z的数据类型是Byte"
print "用z来接受Integer变量除法的结果"

print " "
print "当被除数是260, 除数是257的时候"
y = 260
x = 257
z = y \ x
print "z的值为:" ; z
'最后输出是4

print " "
print "当被除数是200, 除数260的时候"
y = 200
x = 260
z = y \ x
print "z的值为:" ; z
'最后输出是50

print " "
print "当被除数是260, 除数是5的时候"
y = 260
x = 5
z = y \ x
print "z的值为:" ; z
'最后输出是0

print " "
print "当被除数是200, 除数是5的时候"
y = 200
x = 5
z = y \ x
print "z的值为:" ; z
'最后输出是40


End
