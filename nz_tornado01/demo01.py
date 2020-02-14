import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler): #请求处理的类视图
    #继承于RequestHandler类
    def get(self):
        self.write('tornado是一个支持高并发的web框架') #以字符串为参数写入到http的响应中
    def post(self):
        pass


def make_app():
    return tornado.web.Application(
        handlers=[
            (r'/',MainHandler)
        ]
    )

if __name__ == "__main__":
    #启动实例
    app = make_app()
    #监听端口
    app.listen(8000)
    #接收客户端的请求
    tornado.ioloop.IOLoop.current().start()
