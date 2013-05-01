from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

class SignupForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password') 
		

# Create your models here.
