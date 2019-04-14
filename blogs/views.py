from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.models import User

from .models import *
from .forms import *


class PostsList(View):
    def get(self, request, username='', subscribe=''):
        if username and subscribe:
            user = User.objects.get(username=username)
            subscribe_blogs = Subscribe.objects.filter(user=user)
            blog = Blog.objects.get(author=user)
            posts = blog.post_set.all()
        elif username:
            user = User.objects.get(username=username)
            blog = Blog.objects.get(author=user)
            posts = blog.post_set.all()
        else:
            posts = Post.objects.all()
        return render(request, 'blogs/post_list_user.html', context={'posts': posts})

class SubscribePostsList(View):
    def get(self, request, username):

        return render(request, 'blogs/post_list_user.html', context={'posts': posts})


class NewPost(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blogs/new_post.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        blog = Blog.objects.get(author=request.user)
        if bound_form.is_valid():
            cleaned_data = bound_form.cleaned_data
            cleaned_data['blog'] = blog
            new_post = Post.objects.create(**cleaned_data)
            new_post.save()
            return redirect(new_post)
        return render(request, 'blogs/new_post.html', context={'form': bound_form})