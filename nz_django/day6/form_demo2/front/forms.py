from django import forms
from django.core import validators
class Myform(forms.Form):
    # email = forms.EmailField(error_messages={'invalid':'请输入正确的邮箱'})
    # price = forms.FloatField(error_messages={'invalid':'请输入正确的价格'})
    # website = forms.URLField(error_messages={'invalid':'请输入正确的个人网站'})
    email = forms.CharField(validators=[validators.EmailValidator(message="请输入正确的邮箱")])
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3-9]\d{9}',message='请输入正确的手机号')])
    website = forms.CharField(validators=[validators.URLValidator(message="请输入正确的个人主页")])
