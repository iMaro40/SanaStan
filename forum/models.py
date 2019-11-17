import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.





class Post (models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE) #might make own User model?
    topic = models.ForeignKey('ForumTopic',on_delete=models.CASCADE, null = True )
    title = models.ForeignKey('Title',on_delete=models.CASCADE,related_name = 'posts')
    content = models.TextField()
    time_posted = datetime.datetime.now()

    def __str__(self):
        return f' "{self.title}" by {self.author}'

class ForumTopic (models.Model):
    topic = models.CharField(max_length = 100, primary_key = True)

    class Meta:
        ordering = ['topic']

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('topic-titles',args=[str(self.topic)])

class Title (models.Model):
    title = models.CharField(max_length = 100)
    topic = models.ForeignKey('ForumTopic',on_delete=models.CASCADE,null = True,related_name='titles')
    creator = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    opening_post = models.TextField(default =" ")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('title-posts',args=[str(self.topic),str(self.pk)])
