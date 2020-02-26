from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator
class User(models.Model):
    username = models.CharField(max_length=100,validators=[MinLengthValidator(6)])
    password = models.CharField(max_length=100,validators=[MinLengthValidator(6)])
    telephone = models.CharField(max_length=11,validators=[RegexValidator(r'1[3-9]\d{9}',message='请输入正确的手机号')])
    create_time = models.DateTimeField(auto_now_add=True,null=True)