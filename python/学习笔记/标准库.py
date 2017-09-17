# sys模块
#sys 模块包含了系统指定的函数功能
import sys, warnings
print(sys.version_info)

if sys.version_info[0] < 3:
             warnings.warn("Need python 3.0 for this program to run")
else :
             print('Proceed as nomal')


#logging 模块
#如果你想得到一些调试信息或重要信息并将其存储在某个地方，用来检查你的程序程序运行是否是你期望的那样
#  可以用 logging 模块来实现
import os, platform, logging
if platform.platform().startswith('Windows'):
             logging_file = os.path.join('D:/', 'test.log')
else:
             logging_file = os.path.join(os.getenv('HOME'), 'test.log')
print("logfile is {0} -- platform is {1}".format(logging_file, platform.platform()))
logging.basicConfig(
             level = logging.DEBUG,
             format = '%(asctime)s : %(levelname)s : %(message)s',
             filename = logging_file,
             filemode='w' ,
             )
logging.debug("start of the program")
logging.info("Doing something")
logging.warning("Dying now")
