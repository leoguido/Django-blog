from django import forms
from django.forms import models
from .models import Comment, Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text' , 'title' ,)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author' , 'text',)
