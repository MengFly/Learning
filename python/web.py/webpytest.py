# -*- coding: cp936 -*-
import web

import pymysql
        
urls = (
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)

# ����ģ��,����ģ�����Ŀ¼
render = web.template.render('templates')

app = web.application(urls, globals())

class index:
          # ��ȡ������Ĳ���
          def GET(self) :
                    query = web.input()
                    return query

          def POST(self):
                    return "index POST method"

class hello:
          # ��ȡ������ͷ
    def GET(self, name):
        return web.ctx.env

class blog:
          def GET(self):
                    # ����ģ���ļ��������ͬ����ģ���ļ�
                    return  render.hello2()

if __name__ == "__main__":
    app.run()
