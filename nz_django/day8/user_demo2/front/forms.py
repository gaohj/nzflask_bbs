from django import forms
from django.contrib.auth import get_user_model #这个方法功能获取当前项目的用户模型
#读取settings文件中的 AUTH_USER_MODEL = 'front.User'
#front.User 就是我们自定义的用户模型

class LoginForm(forms.ModelForm):
    telephone = forms.CharField(max_length=11)
    remember = forms.IntegerField(required=False)
    class Meta:
        model = get_user_model()
        fields = ['password']