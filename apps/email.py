#导入mail对象
from flask import current_app,render_template
from apps.extensions import mail
from flask_mail import Message
from threading import Thread

def async_send_mail(app,msg):
    #发送邮件需要上下文 新的线程没有上下文 需要手动创建上下文
    with app.app_context():#手动创建上下文
        #发送邮件
        mail.send(message=msg)


#封装函数 用来发送邮件
def send_mail(to,subject,template,**kwargs):
    app = current_app._get_current_object()
    #发送邮件
    msg = Message(subject=subject,recipients=[to],sender=app.config['MAIL_USERNAME'])

    #客户端看到的内容
    msg.body = render_template(template+'.txt',**kwargs)
    #网页看到的内容
    msg.html = render_template(template+'.html',**kwargs)

    #创建线程
    thr = Thread(target=async_send_mail,args=[app,msg])
    #启动线程
    thr.start()

    return thr