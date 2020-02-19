from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100,null=False,unique=True)
    author = models.CharField(max_length=100,null=False)
    price = models.FloatField(default=0,null=False)
    pub_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Book:[name:%s,author:%s,price:%s,pub_time:%s]>' % (self.name,self.author,self.price,self.pub_time)
    class Meta:
        db_table = 'books'
        # ordering = ['-pub_time']