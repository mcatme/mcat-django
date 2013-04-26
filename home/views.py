from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html', )

def bye(request):
    logout(request)
    return render(request, 'bye.html')

def gone(request):
    u = request.user
    logout(request)
    u.delete()
    return render(request, 'gone.html')

def tour(request):
    return render(request, 'tour.html', )

def join(request):
    return render(request, 'join.html', )

def hello(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username, '', password)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
    return render(request, 'dashboard.html')

def about(request):
    return render(request, 'about.html', )

def faq(request):
    return render(request, 'faq.html', )

def contact(request):
    return render(request, 'contact.html', )

def privacy(request):
    return render(request, 'privacy.html', )

def terms(request):
    return render(request, 'terms.html', )

def help(request):
    return render(request, 'help.html', )

