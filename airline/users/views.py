from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'users/user.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            password = password,
            username = username
        )
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            ctx = {'message':'Error identifiants !!!'}
            return render(request, 'users/login.html', ctx)


def logout_view(request):
    logout(request)
    ctx = {'message': 'Logged Out!'}
    return render(request, 'users/login.html', ctx)
