from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')
def user(request):
    return render(request, 'user.html')

def blank(request):
    return render(request, 'blank.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user')  # Redirige al nombre de URL 'user'
        else:
            return render(request, 'login.html', {'error_message': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')  # Ensure an HttpResponse is returned for GET requests

def user_panel(request):
    return None

def login_view(request):
    return None



def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        # Authenticate and login the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user')  # Redirect to the user page
    return render(request, 'register.html')