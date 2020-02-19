from django.db import models
from django.utils.timezone import now
# Create your models here.
class Article(models.Model): #article_article
    # 主键 自增 int 类型
    id = models.AutoField(primary_key=True)
    # 图书名字 name varchar(60)
    name = models.CharField(max_length=100, null=False,db_column='title',unique=True)
    author = models.CharField(max_length=30, null=False)
    price = models.FloatField(null=False, default=0.0)
    # create_time = models.DateTimeField(auto_now_add=True)
    create_time = models.DateTimeField(default=now)
    class Meta:
        db_table = 'articles'
        ordering = ['-create_time']


