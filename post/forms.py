from .models import Post
from django import forms

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'body']
