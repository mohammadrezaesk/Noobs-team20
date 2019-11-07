from django.shortcuts import render
from .models import ContactUs

# Create your views here.
def HomePage(request):
    return render(request, 'Home/homepage.html')
def Contact(request):
    done = 0
    args={'done':done}
    if request.method == "GET":
        return render(request,'Home/contact.html',args)
    elif request.method == "POST":
        title = request.POST['title']
        email = request.POST['email']
        text = request.POST['text']
        if len(text)>=10 and len(text)<=250:
            done = 1
            args = {'done': done}
            contact = ContactUs(title=title, email=email, text=text)
            contact.save()
            return render(request, 'Home/contact.html', args)
        else:
            return render(request, 'Home/contact.html', args)
