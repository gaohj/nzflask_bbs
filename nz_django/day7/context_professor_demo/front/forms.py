from django import forms

from .models import User

class SigninForm(forms.ModelForm):
    def get_errors(self):
        new_errors=[]
        errors = self.errors.get_json_data()
        for messages in errors.values():
            #messages结果是:[{'message': '用户名最少不能少于6位', 'code': 'min_length'}]
            for message_dict in messages:
                #message_dict 结果是字典
                for key,message in message_dict.items():
                    if key == 'message':
                        new_errors.append(message)
        return new_errors
        #['用户名最少不能少于6位', '密码最少不能少于6位']
    class Meta:
        model = User
        fields = ['username','password']
        error_messages = {
            'username':{
                'min_length':'用户名最少不能少于6位'
            },
            'password':{
                'min_length': '密码最少不能少于6位'
            }
        }

class SignupForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=16,min_length=6)
    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError('两次密码输入不一致')
    class Meta:
        model = User
        fields = "__all__"