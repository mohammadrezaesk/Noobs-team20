from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as lgn
from django.contrib.auth import logout as lgt
from django.contrib.auth.decorators import login_required


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
        lgn(request,user)

        return redirect('/')


def Login(request):
    arg = {'error': 0 }
    if request.method == 'GET' and request.user.is_authenticated == False:
        return render(request, 'Accounts/login.html', arg)
    elif request.method == 'GET' and request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        entered_user = User.objects.all()
        for i in entered_user:
            if i.password == password and i.username == username:
                lgn(request, i)
                return redirect('/')
        arg = {'error': 1 }
        return render(request, 'Accounts/login.html', arg)
@login_required
def Logout(request):
    lgt(request)
    return redirect('/accounts/login')
