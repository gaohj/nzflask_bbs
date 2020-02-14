from datetime import datetime,timedelta
import os
import tornado.ioloop
import tornado.web
from tornado.options import define,parse_command_line,options
from app import (
    IndexHandler,
    TindexHandler,
    DbHandler,
    DropHandler,
    AddHandler,
    SelectHandler
)
define('port',default=8081,type=int) #定义默认的启动端口号为8081



def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/',IndexHandler),
            (r'/tindex',TindexHandler),
            (r'/create',DbHandler),
            (r'/drop',DropHandler),
            (r'/add',AddHandler),
            (r'/select',SelectHandler),
        ],autoreload=True,debug=True,template_path=os.path.join(os.path.dirname(__file__),'templates'),static_path=os.path.join(os.path.dirname(__file__),'static')
    )




if __name__ == "__main__":
    #你想添加启动选项 那么我就监听你的选项是什么
    parse_command_line() #监听启动命令 获取选项
    #启动实例
    app = make_app()
    #监听端口
    app.listen(options.port) #获取你设置的端口号
    #接收客户端的请求
    tornado.ioloop.IOLoop.current().start()