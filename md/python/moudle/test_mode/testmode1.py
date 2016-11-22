# -*- coding: cp936 -*-
# 导入模块
# 使用import来带入模块
import math
# 之后就可以使用math模块中的变量和类
print math.pow(2, 0.5)  # 1.41421356237
print math.pi # 3.14159265359
# 如果只想导入用到的math模块中的几个函数，而不是所有函数，可以使用一下语句
from math import pow, sin, log
print pow(2, 10)    # 1024.0
print sin(3.14)     # 0.00159265291649

# 如果使用import导入模块名，必须使用模块名来引用函数，不会出现名称的冲突
# 而使用from...import使用的时候不用使用模块名，势必会出现冲突
# 因此可以使用别名来避免冲突
# 例如：
from math import log
from logging import log as logger
print log(10) # 2.30258509299
logger(10, 'import from logging')
# 这样就可以避免命名冲突了

import os
print os.path.isdir(r'C:\Windows')  # True
print os.path.isfile(r'C:\Windows\notepad.exe') # True

# 动态导入模块
# 如果导入的模块不存在，Python编译器就会报importError错误
# 因为Python是解释性语言，代码运行速度慢，一些关键函数会使用C语言编写
# 例如Python中的StringIO模块和cStringIO模块
# 利用ImportError错误，我们就可以动态导入模块
# 例子：
try :
    from  cStringIO import StringIO
except ImportError :
    from StringIO import StringIO
# 以上代码先尝试从cStringIO导入，如果失败了（比如cStringIO没有安装），就从StringIO里面导入
# try except 就相当于Java里面的try catch

# 使用__future__
# Python的新版本会引入新的功能，但是，实际上这些功能在 上一个老版本中就已经存在了。要‘试用’某一新功能，就可以通过导入__future__模块的某些功能来实现
# 例如Python2.7的整数除法运算结果只能是整数
print 10 / 3    # 3
# 但是在Python3.x已经改进了整数的除法运算,(整数)/(整数)==》浮点数， (整数)//(整数)==》整数
# 要想在Python2.7中引用3.x里面的除法规则，导入__future__的division
from __future__ import division
print 10 / 3    # 3.33333333333
print 10 // 3   # 3

# 安装第三方模块
# Python提供了两种模块管理工具
# easy_install
# pip（推荐，已经内置到Python2.7.9）
# 在命令行输入 pip install (模块名)就可以安装相应的模块了
# 例如 ： pip install web.py
# 可以在Python官方网站搜索模块，找到相应模块名字就可以使用pip来安装了






