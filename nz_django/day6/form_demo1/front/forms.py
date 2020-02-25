from django import forms

class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=6,min_length=2,label='标题',error_messages={"min_length":"最少不能少于2个字节"})
    content = forms.CharField(widget=forms.Textarea,label="内容",error_messages={"required":"必须要传入content字段"})
    email = forms.EmailField(label="邮箱",error_messages={"required":"必须要传入email字段"})
    reply = forms.BooleanField(required=False,label='是否回复')