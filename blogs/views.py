from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

from .models import *


class PostsList(View):
    def get(self, request, username='', subscribe=''):
        if username and subscribe:
            user = User.objects.get(username=username)

            blog = Blog.objects.get(author=user)
            posts = blog.post_set.all()
        elif username:
            user = User.objects.get(username=username)
            blog = Blog.objects.get(author=user)
            posts = blog.post_set.all()
        else:
            posts = Post.objects.all()
        return render(request, 'blogs/post_list_user.html', context={'posts': posts})

