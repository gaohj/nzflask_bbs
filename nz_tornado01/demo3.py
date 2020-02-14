import tornado.ioloop
import tornado.web
from tornado.options import define,parse_command_line,options
define('port',default=8081,type=int) #定义默认的启动端口号为8081
class MainHandler(tornado.web.RequestHandler): #请求处理的类视图
    #继承于RequestHandler类
    def get(self):
        # name = self.get_argument('name',default='kangbazi',strip=True)
        #name = self.get_query_argument('name',default='kangbazi',strip=True)
        # name = self.get_arguments('name',strip=True)
        name = self.get_query_arguments('name',strip=True)
        self.write('helloadadf99999 %s' % name) #以字符串为参数写入到http的响应中
    def post(self):
        #name= self.get_body_argument('username',default='haha',strip=True)
        #http://127.0.0.1:8004  结果 hello haha
        #name= self.get_body_argument('username',default='haha',strip=True)
        name= self.get_body_arguments('username',strip=True)
        password= self.get_body_arguments('password',strip=True)

        self.write('hello %s:%s' % (name,password))


def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/',MainHandler)
        ],autoreload=True,debug=True
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
