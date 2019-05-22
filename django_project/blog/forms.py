from django import forms

from .models import Photo
from .models import Post


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
