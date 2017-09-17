# 爬取京东商城上面的手机图片
import re
import urllib.request

def mkdir(dirname):
             import os
             import os.path
             if os.path.exists(dirname):
                          return
             else :
                          os.makedirs(dirname)

def getimagename(imagename):
             mkdir(r'D:\python\web\image\jingdong\phone')
             print('make dir....')
             return  r'D:\python\web\image\jingdong\phone' + "/" + imagename

#抓取页面的函数
def craw(url, page):
             html1 = urllib.request.urlopen(url).read()
             html1 = str(html1)
             print(html1)
                          
if __name__ ==  '__main__' :
             #for i in range(1, 79):
             url = 'http://list.jd.com/list.html?cat=9987,653,655&page=1' 
             craw(url, 1)
