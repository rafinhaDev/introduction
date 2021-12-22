from django import forms
from django.db.models import fields

from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'content')