from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

input_style = 'w-full py-4 px-6 rounded-xl'

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
    
  username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your username',
    'class': input_style
  }))
  email = forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder': 'Your email',
    'class': input_style
  }))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Your password',
    'class': input_style
  }))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Repeat password',
    'class': input_style
  }))
