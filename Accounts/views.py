from django.shortcuts import render
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
        # user = User('first_name'=firstname,'last_name'=lastname,'username'=username)
        return render(request, 'Accounts/register.html')
