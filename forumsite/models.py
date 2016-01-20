from django.db import models
from django.contrib.auth.models import User as Auth_User
import datetime

# Create your models here.

class Category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    nameCN = models.CharField(max_length=50)
    nameEN = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.nameCN
    
    class Meta():
        db_table = 'Category'

class Thread(models.Model):
    threadid = models.AutoField(primary_key=True)
    categoryid = models.ForeignKey(Category,db_column='categoryid')
    userid = models.ForeignKey(Auth_User,db_column ='userid')
    title = models.CharField(max_length=300)
    content = models.TextField()
    pushtime = models.DateTimeField(default=datetime.datetime.now())
    commentsCount = models.IntegerField(default=0)
    hashcode = models.CharField(max_length=7)
    
    def __unicode__(self):
        return self.title
    
    class Meta():
        db_table = 'Thread'
        ordering = ['-pushtime']
    
class Comment(models.Model):
    commentid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Auth_User,db_column='userid')
    threadid = models.ForeignKey(Thread,db_column='threadid')
    content = models.TextField()
    pushtime = models.DateTimeField(default=datetime.datetime.now())
    
    def __unicode__(self):
        return 'user:' + str(self.userid)
    
    class Meta():
        db_table = 'Comment'
        ordering = ['pushtime']