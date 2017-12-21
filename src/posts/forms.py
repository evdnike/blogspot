from django import forms
from .models import Post, Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment',]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'body']        