from django.db import models
from django.core import validators
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # thumbnail = models.FileField(upload_to='files',validators=[validators.FileExtensionValidator(['jpg','png','jpeg','gif'],message='文件必须是图片')])
    thumbnail = models.FileField(upload_to='%Y/%m/%d',validators=[validators.FileExtensionValidator(['jpg','png','jpeg','gif'],message='文件必须是图片')])