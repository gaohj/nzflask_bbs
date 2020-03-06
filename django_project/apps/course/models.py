from django.db import models
from shortuuidfield import ShortUUIDField
# Create your models here.
class CourseCategory(models.Model):
    name = models.CharField(max_length=100)

class Teacher(models.Model):
    username = models.CharField(max_length=100)
    avator = models.URLField()
    jobtitle = models.CharField(max_length=100)
    profile = models.TextField()


class Course(models.Model):
    title = models.CharField(max_length=200) #标题
    category = models.ForeignKey("CourseCategory",on_delete=models.DO_NOTHING)#分类
    teacher = models.ForeignKey("Teacher",on_delete=models.DO_NOTHING)#教师
    video_url = models.URLField() #视频地址
    cover_url = models.URLField() #封面地址
    price = models.FloatField() #价格
    duration = models.IntegerField() #时长
    profile = models.TextField() #课程简介
    pub_time = models.DateTimeField(auto_now_add=True)

class CourseOrder(models.Model):
    uid = ShortUUIDField(primary_key=True)
    course = models.ForeignKey("Course",on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey("qfauth.User",on_delete=models.DO_NOTHING)
    pub_time = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0)
    #1 支付宝支付  2  微信支付
    istype = models.SmallIntegerField(default=0)
    #1 未支付  2 支付成功
    status = models.SmallIntegerField(default=1)
