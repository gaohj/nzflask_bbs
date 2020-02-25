from django import forms
from django.core import validators
from .models import User

class BaseForm(forms.Form):
    def get_errors(self):
        errors = self.errors.get_json_data() #返回的是一个字典
        new_errors = {} #新字典用来存放最终的结果
        #遍历字典
        for key,message_dicts in errors.items():
            #print(key) #直接作为键存到新字典中
            #print(message_dicts) #遍历列表中元素的message对应的信息
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors

# {'username': [{'message': 'Ensure this value has at least 6 characters (it has 4).', 'code': 'min_length'}], 'telephone': [{'message': '18777777777已经被注册', 'code': ''}], '__all__': [{'message': '两次密码输入不一致', 'code': ''}]}
# {'username':['手机号已经存在','手机号不符合要求'],'telephone':[]}


class Myform(BaseForm):
    # email = forms.EmailField(error_messages={'invalid':'请输入正确的邮箱'})
    # price = forms.FloatField(error_messages={'invalid':'请输入正确的价格'})
    # website = forms.URLField(error_messages={'invalid':'请输入正确的个人网站'})
    email = forms.CharField(validators=[validators.EmailValidator(message="请输入正确的邮箱")])
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3-9]\d{9}',message='请输入正确的手机号')])
    website = forms.CharField(validators=[validators.URLValidator(message="请输入正确的个人主页")])


class RegisterForm(BaseForm):
    username = forms.CharField(max_length=100,min_length=6)
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3-9]\d{9}',message='手机号输入错误')])
    pwd1 = forms.CharField(max_length=30,min_length=6)
    pwd2 = forms.CharField(max_length=30,min_length=6)

    def clean_telephone(self):
        #获取用户输入的手机号 并且是验证以后的
        telephone = self.cleaned_data.get('telephone')
        #查询数据库是否存在
        exists = User.objects.filter(telephone=telephone).exists()
        #如果存在 抛出错误
        if exists:
            raise forms.ValidationError(message="%s已经被注册"%telephone)
        #如果不存在一定要返回 因为要发送到服务器
        return telephone

    #上面是针对一个字段继续验证

    #下面将继续对多个字段验证 需要重写clean方法
    def clean(self):
        #如果走到了clean方法 说明之前的每一个字段都验证成功了
        cleaned_data = super(RegisterForm, self).clean()

        #获取字段
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')

        if pwd1 != pwd2:
            raise forms.ValidationError(message='两次密码输入不一致')
        return cleaned_data  #一定记得返回来

