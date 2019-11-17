from django import forms
from django.contrib.auth.models import User
from forum.models import Title, Post

class TitleCreationForm (forms.ModelForm):

    class Meta:
        model = Title
        fields = ['title', 'opening_post']

class PostCreationForm (forms.ModelForm):

    class Meta:
        model = Post
        fields = ['content']
