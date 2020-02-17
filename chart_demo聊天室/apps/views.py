import tornado.web
import tornado.websocket
#注册
class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        error = ''
        self.render('signup.html',error=error)  #让用户看到注册的页面
    def post(self):
        #接收用户提交的数据
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        #此处应该是从数据库中进行验证现在先省略
        self.write('注册成功')

#登录
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        error = ''
        self.render('signin.html',error=error)  #让用户看到注册的页面
    def post(self):
        #接收用户提交的数据
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        if username in ['kongkong','yiyi','weiwei','longlong'] and password == '123456':
            # self.set_cookie('username',username) #明文
            self.set_secure_cookie('username',username) #密文
            self.render('chat.html',username=username)
        else:
            error = '账户或者密码错误'
            self.render('signin.html',error=error)


#聊天
class ChatHandler(tornado.websocket.WebSocketHandler):
    #创建一个容器 用来接收所有的链接
    user_online = []

    def open(self,*args,**kwargs): #用户登录成功出发这个函数
        self.user_online.append(self) #谁登录成功  进入容器
        for user in self.user_online:
            username = self.get_secure_cookie('username').decode('utf-8')
            user.write_message("系统提示：【%s进入聊天室】" % username)
    def on_message(self, message): #接收前端发过来的消息  然后返回到浏览器
        username = self.get_secure_cookie('username').decode('utf-8')
        for user in  self.user_online:
            user.write_message(u"%s:%s" % (username,message))

    def on_close(self): #如果有谁退出 那么触发该函数
        self.user_online.remove(self)
        for user in self.user_online:
            username = self.get_secure_cookie('username').decode('utf-8')
            user.write_message(u"系统提示：【%s退出聊天室】" % (username))