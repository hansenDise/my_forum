from django.db import models

# Create your models here.

class Thread(models.Model):
    threadid = models.AutoField(primary_key=True)
    userid = models.IntegerField() 
    title = models.CharField(max_length=200)
    content = models.TextField()
    posttime = models.DateTimeField()
    commentcounts = models.IntegerField()
    default_test = models.IntegerField(default=851)
    
    
class Comment(models.Model):
    commentid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    threadid = models.ForeignKey(Thread,db_column='threadid')
    content = models.TextField()
    commenttime = models.DateTimeField()
    targetuserid = models.IntegerField()
    isread = models.BooleanField()       
    