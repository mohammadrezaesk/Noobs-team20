from django.shortcuts import render , redirect
from Home.models import ContactUs
from django.core.mail import send_mail

# Create your views here.
def HomePage(request):
    return render(request, 'Home/homepage.html')


def Contact(request):
    done = 0
    args = {'done': done}
    if not request.POST:
        return render(request, 'Home/contact.html', args)
    else:
        title = request.POST['title']
        email = request.POST['email']
        text = request.POST['text']
        if len(text) >= 10 and len(text) <= 250:
            done = 1
            args = {'done': done}
            contact = ContactUs(title=title, email=email, text=text)
            contact.save()
            TextWithEmail = text + '\n' + email
            send_mail(title,TextWithEmail,"asdsd@gmail.com",['webe19lopers@gmail.com'], fail_silently=False, )
            return redirect('/contact/success')
        else:
            return render(request,'Home/contact.html')



def contactsuccess(request):
    return render(request, 'Home/contactsuccess.html')
