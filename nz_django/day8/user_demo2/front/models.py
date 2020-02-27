from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,AbstractBaseUser,PermissionsMixin
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
    def _create_user(self, telephone,username, email, password, **kwargs):
        if not telephone:
            raise ValueError('The given telephone must be set')
        if not password:
            raise ValueError('The given password must be set')
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(telephone=telephone,username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone,username, email,password, **kwargs):
        kwargs['is_staff'] = False
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone, username=username,email=email, password=password, **kwargs)

    def create_superuser(self, telephone,username, email, password, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
        return self._create_user(telephone=telephone,username=username, email=email, password=password, **kwargs)


# class User(AbstractUser):
#     telephone = models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3-9]\d{9}',message='请输入正确的手机号')],unique=True)
#     school = models.CharField(max_length=60)
#
#     objects = UserManager()
#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'telephone'

class User(AbstractBaseUser,PermissionsMixin):
    telephone = models.CharField(max_length=11,
                                 validators=[validators.RegexValidator(r'1[3-9]\d{9}', message='请输入正确的手机号')],
                                 unique=True)
    email = models.CharField(max_length=100,validators=[validators.EmailValidator(message='邮箱格式不符合要求')],unique=True)
    username = models.CharField(max_length=100,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []


    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_black_list(self):
        return self.objects.filter(is_active=False)


from django.contrib.auth import get_user_model
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('view_article','查看文章'),
        )