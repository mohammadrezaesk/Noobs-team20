from django.shortcuts import render, redirect
from django.contrib.auth import login as lgn
from django.contrib.auth import logout as lgt
from django.contrib.auth.decorators import login_required
from .models import User


# Create your views here.
def Register(request):
    if request.method == "GET":
        return render(request, 'Accounts/register.html')
    elif request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
        user.save()
        return render(request, 'Accounts/register.html')


def Login(request):
    if request.method == 'GET' and request.user.is_authenticated == False:
        return render(request, 'Accounts/login.html')
    elif request.method == 'GET' and request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        entered_user = User.objects.all()
        for i in entered_user:
            if i.password == password:
                lgn(request, i)
                return redirect('/accounts/home')