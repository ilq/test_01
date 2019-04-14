from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

        widgets = {
            'title': forms.TextInput(),
            'body': forms.Textarea(),
        }