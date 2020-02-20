from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return '<Category(id:%s,name:%s)>' % (self.id, self.name)
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('front.FrontUser',on_delete=models.CASCADE,null=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,related_name='articles')
    def __str__(self):
        return '<Article(id:%s,title:%s)>' % (self.id, self.title)
