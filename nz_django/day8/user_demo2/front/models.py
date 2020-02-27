from django.db import models
from django.contrib.auth.models import User,AbstractUser,BaseUserManager
from django.core import validators
from django.dispatch import receiver #接收
from django.db.models.signals import post_save

# class Person(User):
#     # telephone = models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3-9]\d{9}',message='请输入正确的手机号')])
#     #代理模型不能创建字段
#     class Meta:
#         proxy = True #说明Person是User的代理类
#
#     @classmethod
#     def get_blacklist(self):
#         return self.objects.filter(is_active=False)

# class UserExtension(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='extension')
#     telephone = models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3-9]\d{9}',message='请输入正确的手机号')])
#     school = models.CharField(max_length=50)
#
# @receiver(post_save, sender=User)
# def handler_user_extension(sender,instance,created,**kwargs):
#     #如果新创建 添加
#     if created:
#         UserExtension.objects.create(user=instance)
#     #如果修改那么就保存
#     else:
#         instance.extension.save()
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    telephone = models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3-9]\d{9}',message='请输入正确的手机号')],unique=True)
    school = models.CharField(max_length=60)

    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'telephone'
