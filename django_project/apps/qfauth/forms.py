from django import forms
from apps.forms import FormMixin
class LoginForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11,min_length=11)
    password = forms.CharField(max_length=30,min_length=6,error_messages={"max_length":"密码最多不能超过30个字符","min_length":"密码最少不能少于6个字符"})
    remember = forms.IntegerField(required=False)

class RegisterForm(forms.Form,FormMixin):
    pass