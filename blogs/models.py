from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.

class Blog(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=254, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('posts_user_url', kwargs = {'username': self.blog.author.username})


class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # subscribe = models.BooleanField(default=False)


class ReadCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # read_flag = models.BooleanField(default=False)
