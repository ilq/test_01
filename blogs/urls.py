from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsList.as_view(), name='posts_all_url'),
    path('blog/new_post/', NewPost.as_view(), name='new_post_url'),
    path('blog/<str:username>', PostsList.as_view(), name='posts_user_url'),
]