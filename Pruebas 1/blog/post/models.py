from typing import Text
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('auth.User' , on_delete = models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True , null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):    
        return self.comments.filter(approved=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('post.Post' , on_delete=models.CASCADE , related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def approve_comment(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text