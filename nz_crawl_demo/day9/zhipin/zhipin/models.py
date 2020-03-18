#将 ip 和 端口号进行拼接  时间转成datetime类型 判断是否过期
#{'ip': '58.218.92.73', 'port': 4898, 'expire_time': '2020-03-18 15:23:02', 'city': '聊城市', 'isp': '联通', 'outip': '119.178.113.112'}
from datetime import datetime,timedelta
class ProxyModel(object):
    def __init__(self,data):
        self.ip = data['ip']
        self.port = data['port']
        self.expire_str = data['expire_time']
        #2020-03-18 15:23:02
        date_str,time_str = self.expire_str.split(" ")
        year,month,day = date_str.split("-")
        hour,minute,seconds = time_str.split(":")
        self.expire_time = datetime(year=int(year),month=int(month),day=int(day),hour=int(hour),minute=int(minute),second=int(seconds))
        self.proxy = "https://{}:{}".format(self.ip,self.port)
        self.blacked = False
    @property
    def is_expiring(self):
        now = datetime.now()
        if(self.expire_time-now) < timedelta(seconds=5):
            return True
        else:
            return False
