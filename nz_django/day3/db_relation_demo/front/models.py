from django.db import models

# Create your models here.
class FrontUser(models.Model):
    username = models.CharField(max_length=50,null=False,blank=False)
    password = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return '<FrontUser(id:%s,username:%s)>'% (self.id,self.username)
    class Meta:
        db_table = 'front_user'

class UserExtension(models.Model):
    school= models.CharField(max_length=100)
    user = models.OneToOneField("FrontUser",on_delete=models.CASCADE,related_name='extension')

    def __str__(self):
        return '<FrontUser(id:%s,school:%s,user_id:%s)>' % (self.id,self.school,self.user.id)
