# -*- coding: cp936 -*-
# ����ģ��
# ʹ��import������ģ��
import math
# ֮��Ϳ���ʹ��mathģ���еı�������
print math.pow(2, 0.5)  # 1.41421356237
print math.pi # 3.14159265359
# ���ֻ�뵼���õ���mathģ���еļ������������������к���������ʹ��һ�����
from math import pow, sin, log
print pow(2, 10)    # 1024.0
print sin(3.14)     # 0.00159265291649

# ���ʹ��import����ģ����������ʹ��ģ���������ú���������������Ƶĳ�ͻ
# ��ʹ��from...importʹ�õ�ʱ����ʹ��ģ�������Ʊػ���ֳ�ͻ
# ��˿���ʹ�ñ����������ͻ
# ���磺
from math import log
from logging import log as logger
print log(10) # 2.30258509299
logger(10, 'import from logging')
# �����Ϳ��Ա���������ͻ��

import os
print os.path.isdir(r'C:\Windows')  # True
print os.path.isfile(r'C:\Windows\notepad.exe') # True

# ��̬����ģ��
# ��������ģ�鲻���ڣ�Python�������ͻᱨimportError����
# ��ΪPython�ǽ��������ԣ����������ٶ�����һЩ�ؼ�������ʹ��C���Ա�д
# ����Python�е�StringIOģ���cStringIOģ��
# ����ImportError�������ǾͿ��Զ�̬����ģ��
# ���ӣ�
try :
    from  cStringIO import StringIO
except ImportError :
    from StringIO import StringIO
# ���ϴ����ȳ��Դ�cStringIO���룬���ʧ���ˣ�����cStringIOû�а�װ�����ʹ�StringIO���浼��
# try except ���൱��Java�����try catch

# ʹ��__future__
# Python���°汾�������µĹ��ܣ����ǣ�ʵ������Щ������ ��һ���ϰ汾�о��Ѿ������ˡ�Ҫ�����á�ĳһ�¹��ܣ��Ϳ���ͨ������__future__ģ���ĳЩ������ʵ��
# ����Python2.7����������������ֻ��������
print 10 / 3    # 3
# ������Python3.x�Ѿ��Ľ��������ĳ�������,(����)/(����)==���������� (����)//(����)==������
# Ҫ����Python2.7������3.x����ĳ������򣬵���__future__��division
from __future__ import division
print 10 / 3    # 3.33333333333
print 10 // 3   # 3

# ��װ������ģ��
# Python�ṩ������ģ�������
# easy_install
# pip���Ƽ����Ѿ����õ�Python2.7.9��
# ������������ pip install (ģ����)�Ϳ��԰�װ��Ӧ��ģ����
# ���� �� pip install web.py
# ������Python�ٷ���վ����ģ�飬�ҵ���Ӧģ�����־Ϳ���ʹ��pip����װ��






