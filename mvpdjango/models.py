from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, PasswordInput, TextInput

class SignupForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password') 
		widgets = {
			'username': TextInput(attrs={'placeholder': 'Username'}),
			'email': TextInput(attrs={'placeholder': 'Email'}),
			'password': PasswordInput(attrs={'placeholder' : 'Password'}),
		}
		
class LoginForm(forms.Form):
		username = forms.CharField(
			widget=forms.TextInput(attrs={'placeholder': 'Username'}))
		password = forms.CharField(
			widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

# Create your models here.
