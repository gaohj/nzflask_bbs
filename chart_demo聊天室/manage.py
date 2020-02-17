import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define,options,parse_command_line
from utils.settings import TEMPLATE_PATH,STATIC_PATH
from apps.views import RegisterHandler,LoginHandler,ChatHandler

define('port',default=8080,help='default port',type=int)

def make_app():
    return tornado.web.Application(handlers=[
        (r'/signup/',RegisterHandler),
        (r'/signin/',LoginHandler),
        (r'/chat/',ChatHandler),
    ],autoreload=True,debug=True,template_path=TEMPLATE_PATH,static_path=STATIC_PATH,cookie_secret='adfafa12sad=-1223'
)

if __name__ == "__main__":
    parse_command_line()
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port,address='0.0.0.0')
    tornado.ioloop.IOLoop.instance().start()