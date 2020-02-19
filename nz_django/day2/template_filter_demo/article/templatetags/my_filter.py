from datetime import datetime
from django import template

register = template.Library()

@register.filter
def time_since(value): #过滤器最多有两个参数
    #value 可以是我们文章的发表时间
    #这个过滤器就好比是微博 发布于 刚刚 几分钟之前 几小时以前
    # 将发表的时间 跟现在的时间进行对比
    #判断value是否是个日期 不是 原样返回
    if not isinstance(value,datetime):
        return value
    now = datetime.now()
    timestamp = (now-value).total_seconds() #转成秒数进行对比
    if timestamp < 60:
        return '刚刚'
    elif timestamp >= 60 and timestamp< 60*60:
        minutes = int(timestamp/60)
        return "%s分钟前" % minutes
    elif timestamp >= 60*60 and timestamp< 60*60*24:
        hours = int(timestamp/60/60)
        return "%s小时前" % hours
    elif timestamp >= 60*60*24 and timestamp< 60*60*24*30:
        days = int(timestamp/60/60/24)
        return "%s天前" % days
    else:
        return value.strftime("%Y-%m-%d %H:%M")

