#服务端
import tornado.httpserver
import tornado.httpclient
#客户端
import tornado.gen
import tornado.web
import tornado.ioloop
from tornado.options import define,options,parse_command_line

define('port',default=8080,help='如果命令行中你没有写port那么就8080',type=int)

#同步 发送请求  阻塞  直到服务器响应  新版本不支持了  全面拥抱asyncio

class IndexHandler(tornado.web.RequestHandler):
    # def get(self):
    @tornado.gen.coroutine
    def get(self):
    # async def get(self):
        q = self.get_argument('q')
        # client = tornado.httpclient.HTTPClient()
        client = tornado.httpclient.AsyncHTTPClient()
        req = yield from client.fetch("https://cn.bing.com/search?q=%s" % q)
        # req = await client.fetch("https://cn.bing.com/search?q=%s" % q)
        res = req.body
        self.write(
            """
            <div style='text-align:center'>
                <div style='font-size:20px'>
                    %s
                </div>
            </div>
            
            """
        % res)
def make_app():
    return tornado.web.Application(handlers=[
        (r'/async/',IndexHandler),
    ],autoreload=True,debug=True)


if __name__ == "__main__":
    #解析命令行中的参数
    parse_command_line()
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    http_server.start(1)
    tornado.ioloop.IOLoop.instance().start()
