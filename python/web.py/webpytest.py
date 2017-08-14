# -*- coding: cp936 -*-
import web

import pymysql
        
urls = (
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)

# 设置模版,定义模版的主目录
render = web.template.render('templates')

app = web.application(urls, globals())

class index:
          # 获取到请求的参数
          def GET(self) :
                    query = web.input()
                    return query

          def POST(self):
                    return "index POST method"

class hello:
          # 获取到请求头
    def GET(self, name):
        return web.ctx.env

class blog:
          def GET(self):
                    # 引用模版文件夹下面的同名的模版文件
                    return  render.hello2()

if __name__ == "__main__":
    app.run()
