from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return '<Category(id:%s,name:%s)>' % (self.id, self.name)


#标签跟文章是多对多的关系

class Tag(models.Model):
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField('Article',related_name='tags')
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('front.FrontUser',on_delete=models.CASCADE,null=True,related_name='u_articles',related_query_name='u_a')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,related_name='articles')
    def __str__(self):
        return '<Article(id:%s,title:%s)>' % (self.id, self.title)
