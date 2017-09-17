import urllib.request

def mkdir(dirname):
             import os
             import os.path
             if os.path.exists(dirname):
                          return
             else :
                          os.makedirs(dirname)

def savefile(filename,content):
             filepath = getsavefile(filename)
             try:
                          with open(filepath, 'wb') as f:
                                       f.write(content)
             except Exception as e:
                          print('file write cause a exception')

def getsavedir() :
             mkdir(r'D:\python\web')
             return  r'D:\python\web'

def getsavefile(filename) :
             return getsavedir() + "/" + filename

# 获取网页的信息,并将网页信息保存在文件中
def get_web_content_and_save(url, filename):
             file = urllib.request.urlopen(url, timeout=3)
             data = file.read()
             dataline = file.readline()
             savefile(filename, data)

def save_web_content_2_file(url, filename):
             #直接写入本地文件
             filename = urllib.request.urlretrieve(url, filename =getsavefile(filename))
             # 清除缓存
             urllib.request.urlcleanup()

#headers属性(模拟浏览器)(这里使用Chrom浏览器的User-Agent
def get_u_a_headers() :
             user_key = 'User-Agent'
             user_value = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36'
             headers = (user_key, user_value)
             return headers

#1.使用build_opener()修改报头
def use_u_a_headers1(url):
             headers = get_u_a_headers()
             opener = urllib.request.build_opener()
             opener.addheaders = [headers]
             return opener.open(url, timeout=3).read()

# 2.使用add_header()添加报头
def use_u_a_headers2(url):
             req = urllib.request.Request(url)
             headerkey, headervalue = get_u_a_headers()
             req.add_header(headerkey, headervalue)
             return urllib.request.urlopen(req, timeout = 3).read()



# 保存百度搜索结果
def save_baidu_search(key) :
             url = 'http://www.baidu.com/s?wd='
             # 对要查询的问题进行编码
             key_code = urllib.request.quote(key)
             url_all = url + key_code
             data = use_u_a_headers2(url)
             savefile('baidusearch'+key+'.html', data)

# 使用代理服务器
def use_proxy(proxy_addr, url):
             proxy = urllib.request.ProxyHandler({'http':proxy_addr})
             opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
             urllib.request.install_opener(opener)
             data = use_u_a_headers2(url)
             return data

# 开Log
def open_log():
             httphd = urllib.request.HTTPHandler(debuglevel=1)
             httpshd = urllib.request.HTTPHandler(debuglevel=1)
             opener = urllib.request.build_opener(httphd, httpshd)
             urllib.request.install_opener(opener)

if __name__ == '__main__' :
            url1 = "http://www.baidu.com"
            url2 = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
            url3 = 'http://www.cnblogs.com/dkblog/archive/2011/02/24/1980651.html'
            get_web_content_and_save(url1, '1.html')
            save_web_content_2_file(url3, '3.html')
            content = use_u_a_headers1(url2)
            savefile('2.html', content)
            content = use_u_a_headers2(url3)
            savefile('4.html', content)
            save_baidu_search("王朋飞")

            # 测试代理服务器
            proxy_addr = '61.135.217.7:80'
            data = use_proxy(proxy_addr, url3)
            savefile('5.html', data)

            
            
