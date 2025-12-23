from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment
 
class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']
 
 
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
 
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']