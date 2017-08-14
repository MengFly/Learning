# -*- coding: utf-8 -*-
# 文件操作
# Python 文件打开方式

# 文件打开方法：open(name[, mode [buff]])
# name : 文件的路径
# mode : 打开方式
# buff : 设置的缓冲大小

# 文件读取方式：read([size]) : 读取文件（读取size个字节，默认是读取全部）
# readline([size]):读取一行
# readlines([size]):读取完文件，返回每一行所组成的列表

# 文件写入方式：
# write(str) : 将字符串写入文件
# writelines(squence_of_strings):写多行到文件（squence_of_strings:每一行组成的列表）

# 为了测试，在同目录下面创建一个文件：hello_py.txt
# 文件内容：I Love Py
# 写一个函数来获取文件中的内容
def get_file_content(fileName) :
    with open(fileName) as f :
        return f.read()
try :
    f = open('hello_py.txt')
    c = f.read()
    print c
    f.close()# 文件使用完毕之后一定要关闭
except IOError, e :
    print '当前目录没有hello_py.txt这个文件， 创建它，并给文件添加文字I Love Py'
    import time
    time.sleep(3)
    exit()


# 也可以这样
with open('hello_py.txt') as f2 :
    print f2.read()

# 文件打开方式：
# 即open里面的mode参数
# 'r'： 只读方式打开 ： 文件必须存在
# 'w'： 只写方式打开 ： 文件不存在创建文件，文件存在则清空文件内容
# 'a'： 追加方式打开 ： 文件不存在则创建文件
# 'r+/w+' 读写方式打开
# 'a+'  追加和读写方式打开
# 'rb', 'wb', 'ab', 'rb+', 'wb+', 'ab+': 二进制方式打开（适用于一些图片文件的打开）

f3 = open('test.txt', 'w') # 以只写方式打开，文件不存在则创建文件，文件存在则清空文件内容
f3.write('hello Py')
# print f3.read()   这行会报错，因为文件是以只写方式打开的，不可读
f3.close()
print get_file_content('test.txt')  # hello Py
# 说明内容已经写入了文件
# 下面不写内容，打开文件看看
f4 = open('test.txt', 'w')
f4.close()
print get_file_content('test.txt')
# 没有打印东西。说明文件里面的内容被清空了

# 以追加方式来打开
f5 = open('hello_py.txt', 'a')
f5.write(' really')
f5.close()
print get_file_content('hello_py.txt')  # I Love Py  really
# 说明以追加方式不会清空文件内容

# 当使用w+ 方式打开的时候，虽然有了读写权限，但是依旧会把文件给清空
# 以r+ 的方式不会清空文件内容

# 文件读取
f6 = open('hello_py.txt')
# print f6.readline()
print f6.readline(2)    # I 
print f6.readline(2)    # Lo
print f6.readline()     # ve Py  really  really
# 上面的说明读取文件的时候下次读取会从上次读取的位置开始读取
# 也就是说使用连续使用两次read的话，第一次会读取所有内容，而第二次将什么也读取不到
f6.close()
print get_file_content('hello_py.txt')

# 使用迭代器读取文件iter(推荐，节省内存)
# 例子：
f7 = open('hello_py.txt')
iter_f = iter(f7) # 将文件转换成迭代器
lines = 0
for line in iter_f :
    lines += 1
    print line # I Love Py  really  really 
print lines # 1
f7.close()


# 文件写入
# write(str) 将字符串写入文件
# writelines(sequence_of_strings) 写多行道文件，参数为可迭代的对象
f8 = open('hello_py.txt', 'w')
f8.write('I Love PY.')
f8.close()
print get_file_content('hello_py.txt') # I Love PY.

f9 = open('hello_py.txt', 'r+')
f9.write('I Love PY. ')
f9.writelines('really')
# f9.writelines((1, 2, 3))这样是不可以的，我们必须传入的是以字符串为元素的可迭代对象
f9.writelines(('1', '2', '3')) # 这样是可以的
f9.close()
print get_file_content('hello_py.txt') # I Love PY. really123

# f10 = open('hello_py.txt', 'a')
# f10.write('really')
# print get_file_content('hello_py.txt')     # I Love PY. really123 还是之前的内容，文件没变化
# 如果只是打开了文件，写入内容，而不去调用close()或flush()方法，则不会向文件中写入内容
# 我们调用write方法的时候只是把要写入的内容放在了系统的缓冲区里面
# 只有我们调用close()或flush()方法的时候，系统才会把缓冲区里面的内容写入文件

# Python写磁盘的时机
# 1、主动调用close()或者flush()方法，写缓存道磁盘
# 2、写入的数据大于或者等于写缓存，写缓存自动同步到磁盘
# 例子：
f11 = open('hello_py.txt', 'a')
print get_file_content('hello_py.txt') # I Love PY. really123
f11.write('  buffer test')
print get_file_content('hello_py.txt') # I Love PY. really123
f11.flush()
print get_file_content('hello_py.txt') # I Love PY. really123  buffer test
f11.close()
print get_file_content('hello_py.txt') # I Love PY. really123  buffer test
# 从上面的例子可以看到只有调用flush的时候内容才写入到文件里面


# Python文件为什么要关闭
# 1、强写缓存同步到磁盘
# 2、linux系统中每个进程打开文件的个数是有限的
# 3、如果打开文件数到达了系统限制，再打开文件就会失败

# Python 写入和读取的问题
# 1、写入文件后，必须打开文件才能读取写入的内容
# 2、读取文件后，无法重新再次读取读过的内容（在前面的笔记中有这个例子）
# 文件读写的时候文件中的指针会移动，文件的读取或是写入都依靠这个指针来进行定位
# 例如我读了三个位置，文件指针就在第三个位置，假如再进行写或读的时候就会从文件指针的地方即（第三个位置之后）进行操作

# 文件指针
# Python文件指针操作
# seek(offset[, whence]) : 移动文件指针
# offset: 偏移量， 可以为负数
# whence：偏移的相对位置（即从哪里开始偏移）
# whence :  os.SEEK_SEt: 相对文件的起始位置 0
#           os.SEEK_CUR: 相对文件的当前位置 1
#           os.SEEK_END: 相对文件的结尾位置 2
# 例子：
f12 = open('hello_py.txt', 'r+')
import os
# tell 函数返回当前文件指针的偏移量
print f12.tell() # 0
print f12.read(3) # I L
print f12.tell() # 3    文件指针移动到了三的位置
# 把文件指针置于起始位置
f12.seek(0, os.SEEK_SET)
print f12.tell() # 0 文件指针已经重置回去了
print f12.read(3) # I L
# 将文件指针置于结尾
f12.seek(0, os.SEEK_END)
print f12.tell()    # 33    (说明文件总共33个字节)
f12.seek(-5, os.SEEK_CUR)
print f12.tell()    # 28
# 如果偏移量大于文件大小就会有错误
# f12.seek(-35, os.SEEK_END) IOError: [Errno 22] Invalid argument
f12.close()

# Python 文件属性
# file.fileno() : 文件描述符
# file.mode : 文件打开权限
# file.encoding : 文件的编码格式
# file.closed : 文件是否关闭（前面的笔记中有）
# 例子： 
f13 = open('hello_py.txt')  # 以只读方式打开
print f13.fileno() # 3
print f13.mode  # r
print f13.encoding # None
print f13.closed # False
f13.close()

# Python标准文件
# 文件标准输入： sys.stdin
# 文件标准输出： sys.stdout
# 文件标准错误： sys.stderr
import sys
print type(sys.stdin) # <class 'idlelib.PyShell.PseudoInputFile'>
# 就是说当我们的命令行接收参数的时候会调用sys.stdin
# 当我们调用print 的时候会自动调用sys.srdout.write()函数

# 编码格式
# 文件的默认编码是ASCII码格式的，当我们想要向文件里面写入中文的时候就会有错误
# 例如f.write(u'文字') # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-3: ordinal not in range(128)
# 想要向文件中写入文字，有两种方式
# 1、将中文进行转码，转码为utf-8格式的，再进行输入
# 2、将文件以utf-8格式打开，可以直接写入中文
# 例子：第一种方式
f14 = open('hello_py.txt', 'a+')
a = unicode.encode(u'文字', 'utf-8')
f14.write(a)
f14.close()
print get_file_content('hello_py.txt') # 文字 PY. really123  buffer test
# 例子，第二种方式：以utf-8格式打开文件
import codecs
f15 = codecs.open('hello_py.txt', 'a+', 'utf-8')
f15.write(u'另一个文字')
f15.close()
print get_file_content('hello_py.txt') # I Love PY. really123  buffer test文字另一个文字

# 使用os模块进行文件操作
# 使用os模块打开文件：os.open(filename, flag, [, mode]) : 打开文件
# flag:文件打开方式：
#   os.O_CREAT : 创建文件
#   os.O_RDONLY : 只读方式打开
#   os.O_WRONLY : 只写方式打开
#   os._RDWR : 读写方式打开

# 使用os模块对文件进行操作
# os.read(fd, buffersize) : 读取文件
# os.write(fd, string): 写入文件
# os.lseek(fd, pos, how) : 文件指针操作
# os.close(fd) : 关闭文件
# 例子：
import os
fd = os.open('hello_py.txt', os.O_RDWR)
os.lseek(fd, 0, os.SEEK_END)
n = os.write(fd, 'hello')
# 重定位
l = os.lseek(fd, 0, os.SEEK_SET)
print l # 0     lseek函数返回的就是当前文件指针所在的位置
print os.read(fd, 10)   # I Love PY.
os.close(fd)

# os模块中方法：
# access(path, mode) 判断该文件的权限： F_OK存在，权限：R_OK, W_OK, X_OK(执行权限)
# 例子 ：
print os.access('hello_py.txt', os.F_OK)    # True
print os.access('hello_py.txt', os.W_OK)    # True
print os.access('hello_py.txt', os.R_OK)    # True
print os.access('hello_py.txt', os.X_OK)    # True
# 表明上面的文件存在，可读，可写，可执行

# listdir(path) 返回当前文件目录下的所有文件组成的列表
# remove(path) 删除文件
# rename(old, new) 修改文件名或者目录名
# mkdir(path[, mode]) 创建目录
# makedirs(path[, mode]) 创建多级目录
# removedirs(paeh) 删除多级目录
# rmdir(path) 删除目录，（目录必须为空目录）
print os.listdir('./') # 返回当前文件夹下面的文件名的列表

# os.path 模块方法介绍
# exists(path) 当前路径是否存在
# isdir(s)  是否是一个目录
# isfile(path) 是否是一个文件
# getsize(filename) 返回文件的大小
# dirname(p) 返回路径的目录
# basename(p) 返回路径的文件名



# python文件练习
# 使用Python管理ini文件： 实现查询，添加，删除，保存
# ini 配置文件格式
# 节 [session]
# 参数（键 = 值） name = value
# 例子：
# [port]
#   port1=8000
#   port2=8001
# 先来创建一个文件
import os
f = os.open('study.ini', os.O_CREAT|os.O_RDWR)
os.write(f, '[userinfo]\n')
os.write(f, 'name = zhangsan\npwd = abc\n')
os.write(f, '[study]\n')
os.write(f, 'python_base = 15\npython_junior = 20\nlinux_base = 15\n')
os.close(f)

# 这个模块是专门用于读取和存储ini配置文件的
import ConfigParser
cfg = ConfigParser.ConfigParser()
print cfg.read('study.ini') # ['study.ini']
print cfg.sections()    # 获取所有的节
# ['userinfo', 'study']

# 获取所有节的属性
for se in cfg.sections() :
    print se
    print cfg.items(se)
# userinfo
# [('name', 'zhangsan'), ('pwd', 'abc')]
# study
# [('python_base', '15'), ('python_junior', '20'), ('linux_base', '15')]

# 修改条目
cfg.set('userinfo', 'pwd', '1234567') # 修改userinfo下面的pwd属性
# 添加条目
cfg.set('userinfo', 'emali', 'www.wangpengfei99@gmail.com')
# 删除条目
cfg.remove_option('userinfo', 'email') # 删除userinfo 下面的email属性

# 例子（一个类来管理ini文件）
import os
import os.path
import ConfigParser
class student_info(object) :
    
    def __init__(self, recordfile) :
        self.logfile = recordfile   # 定义配置文件的名称
        self.cfg = ConfigParser.ConfigParser()  # 初始化配置文件管理类

    def cfg_load(self) :
        self.cfg.read(self.logfile)  # 加载文件的内容

    def cfg_dump(self) :    # 打印配置文件的所有信息
        se_list = self.cfg.sections()
        print '=======================>'
        for se in se_list :
            print se
            print self.cfg.items(se)
        print '=======================>'

    def delete_item(self, section, key) : # 删除一项
        self.cfg.remove_option(section, key)

    def delect_section(self, section) :
        self.cfg.remove_section(section)

    def add_section(self, section) :
        if(not self.cfg.has_section(section)) :
            self.cfg.add_section(section)

    def set_item(self, section, key, value) :
        if(not self.cfg.has_section(section)) :
            self.cfg.add_section(section)
        self.cfg.set(section, key, value)

    def save(self) :
        with open(self.logfile, 'w') as fp :
            self.cfg.write(fp)

# 测试我们写的类
if __name__ == '__main__' :
    info = student_info('student_info.ini')
    info.cfg_load()
    info.cfg_dump()
    info.add_section('userinfo')
    info.set_item('userinfo', 'pwd', 'abc')
    info.cfg_dump()
    info.add_section('login')
    info.set_item('login', '2016-07-18', '20')
    info.cfg_dump()
    info.save()
    
# 查看文件内容：
with open('student_info.ini', 'r') as f :
    print f.read()
# [userinfo]
# pwd = abc

# [login]
# 2016-07-18 = 20







































