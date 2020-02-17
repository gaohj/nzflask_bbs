import tornado.web
import tornado.ioloop
import tornado.httpclient

class AsyncHandler(tornado.web.RequestHandler):
    @tornado.web.gen.coroutine #允许在http请求中执行其它的任务
    def get(self, *args, **kwargs):
        q = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        response =yield client.fetch('https://cn.bing.com/search?q=%s' % q)
        # self.write(
        #     """
        #         <div style='text-align:center'>
        #             <div style='font-size:18px'>
        #                 %s
        #             </div>
        #         </div>
        #     """ % (response.body))
        print(response)
        self.write("异步测试")
def make_app():
    return tornado.web.Application(handlers=[
        (r'/async/',AsyncHandler)
    ],autoreload=True,debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8088)
    tornado.ioloop.IOLoop.current().start()