from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as lgn
from django.contrib.auth import logout as lgt
from django.contrib.auth.decorators import login_required


# Create your views here.
def Register(request):
    error = 0
    users = User.objects.all()
    args = {'error':0}
    if request.method == "GET" and request.user.is_authenticated == False:
        return render(request, 'Accounts/register.html',args)
    elif request.method == 'GET' and request.user.is_authenticated == True:
        return redirect('/')
    elif request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        for user in users :
            if user.username == username:
                error +=2
        if password2 != password1 :
            error += 1
        if error == 1:
            msg = "گذرواژه و تکرار گذرواژه یکسان نیستند"
            args = {'msg': msg,'error':1}
            return render(request, 'Accounts/register.html', args)
        elif error == 2:
            msg = "نام کاربری شما در سیستم موجود است"
            args = {'msg': msg,'error':1}
            return render(request, 'Accounts/register.html', args)
        elif error == 3:
            msg = "نام کاربری شما در سیستم موجود است گذرواژه و تکرار گذرواژه یکسان نیستند"
            args = {'msg':msg,'error':1}
            return render(request,'Accounts/register.html',args)
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
    return redirect('/')


@login_required
def Profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def EditProfile(request):
    if request.method == "GET":
        return render(request, 'Accounts/editprofile.html')
    else:
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        request.user.first_name = fname
        request.user.last_name = lname
        request.user.save()
        return redirect('/accounts/profile')

@login_required
def Panel(request):
    return render(request,'Accounts/panel.html')