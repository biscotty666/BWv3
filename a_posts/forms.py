from django.forms import ModelForm
from django import forms
from .models import *

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'art', 'body', 'tags']
        labels = {
            'body': 'Article',
            'tags': 'Category',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add markdown...', 'class': 'text-xl'}),
            'url': forms.TextInput(attrs={'placeholder': 'Add url ...'}),
            'tags': forms.CheckboxSelectMultiple(),
            'art': forms.FileInput(),
        }
        
class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'art', 'tags']
        labels = {
            'body' : 'Article',
            'tags': 'Category',
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add markdown...', 'class': 'text-xl'}),
            'tags': forms.CheckboxSelectMultiple(),
            'art': forms.FileInput(),
        }

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder':'Add comment ...'})
        }
        labels = {
            'body': ''
        }
        
class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder':'Add reply ...', 'class': "!text-sm"})
        }
        labels = {
            'body': ''
        }