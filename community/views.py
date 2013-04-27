from django.shortcuts import render
from django.contrib.auth.models import User

def dashboard(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', { 'users': users })
