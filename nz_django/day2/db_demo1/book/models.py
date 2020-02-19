from django.db import models

# Create your models here.
class Book(models.Model):
    #主键 自增 int 类型
    id = models.AutoField(primary_key=True)
    #图书名字 name varchar(60)
    name = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=30,null=False)
    price = models.FloatField(null=False,default=0.0)

class Publisher(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    numbered = models.IntegerField(db_column='nums')

class Student(models.Model):
    name = models.CharField(max_length=30,null=False)
    age = models.IntegerField(default=18)

    class Meta:
        db_table = 'stu' #默认在数据库中的表名是
        #应用名称_模型名字小写
        #写了db_table 就以这个名字为准
        #select * from users where id>10 order_by age;
        ordering = ['id']


