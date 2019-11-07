from django.shortcuts import render


# Create your views here.
def Register(request):
   if request.method == "GET":
       return render(request,'Accounts/register.html')