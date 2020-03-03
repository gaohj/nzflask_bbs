from django import forms
from apps.forms import FormMixin
from django.core import validators
from .models import User
class LoginForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11,min_length=11)
    password = forms.CharField(max_length=30,min_length=6,error_messages={"max_length":"密码最多不能超过30个字符","min_length":"密码最少不能少于6个字符"})
    remember = forms.IntegerField(required=False)

class RegisterForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11, min_length=11,validators=[validators.RegexValidator(r'1[3-9]\d{9}',message="请输入正确的手机号")])
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(max_length=30,min_length=6,error_messages={"max_length":"密码最多不能超过30个字符","min_length":"密码最少不能少于6个字符"})
    password2 = forms.CharField(max_length=30,min_length=6,error_messages={"max_length":"密码最多不能超过30个字符","min_length":"密码最少不能少于6个字符"})
    img_captcha = forms.CharField(max_length=4,min_length=4)
    sms_captcha = forms.CharField(max_length=4,min_length=4)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('两次密码输入不一致')

        telephone = cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            forms.ValidationError('该手机号已经被注册')
        return cleaned_data



