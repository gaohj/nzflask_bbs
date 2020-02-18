from django.urls import register_converter
# 写一个类 继承自object
class CategoryConverter(object):
# 在类中定义一个属性 regex 限制url规则的正则表达式
    regex = r'\w+|(\w+\+\w+)+'
#  实现  to_python 方法 这个方法用来将url值转换传给 视图函数
    def to_python(self,value):
        #将 django+flask+tornado => [django,flask,tornado]
        result = value.split('+')
        return result
# 实现 to_url方法   这个方法 用来在url反转的时候 将  传进来的参数转化后拼接成正确的url
    def to_url(self,value):
    # [django,flask,tornado] => django+flask+tornado
        if isinstance(value,list):
            result = "+".join(value)
            return result
        else:
            raise RuntimeError('转换成url的时候参数必须是列表')
#将其 注册到 django 中
register_converter(CategoryConverter,'cate')




