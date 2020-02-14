import tornado.ioloop
import tornado.web
from tornado.options import define,parse_command_line,options
define('port',default=8081,type=int) #定义默认的启动端口号为8081
class MainHandler(tornado.web.RequestHandler): #请求处理的类视图
    #继承于RequestHandler类
    def get(self):
        self.write('命令行启动的时候我可以自定义端口号') #以字符串为参数写入到http的响应中
    def post(self):
        pass


def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/',MainHandler)
        ]
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
