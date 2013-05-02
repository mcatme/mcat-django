from mvpdjango.models import SignupForm, LoginForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

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

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					render(request, 'success.html')
				else:
					render(request, 'invalid-login.html')
	else:
		form = LoginForm()
	return render(request, 'login.html', { 'login_form': form})	

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

def success(request):
	return render(request, 'success.html', )

def signup_form(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			new_user = User.objects.create_user(username, email, password)	
			new_user.save()
			return HttpResponseRedirect('/success/')
	else:
		form = SignupForm()
	return render(request, 'home.html', { 'signup_form' : form })



