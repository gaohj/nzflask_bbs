from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Category(id:%s,name:%s)" %(self.id,self.name)

    class Meta:
        db_table = 'category'

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,related_query_name='articles')
    create_time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return "Article(id:%s,title:%s,category_name:%s)" %(self.id,self.title,self.category.name)

    class Meta:
        db_table = 'article'