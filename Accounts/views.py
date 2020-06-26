from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as lgn, authenticate
from django.contrib.auth import logout as lgt
from django.contrib.auth.decorators import login_required
from Home.models import Course
from Accounts.models import x
from django.db.models import Q
from Accounts.models import Profile as ProfileModel


# Create your views here.
def Register(request):
    error = 0
    users = User.objects.all()
    args = {'error': 0}
    if request.method == "GET" and request.user.is_authenticated == False:
        return render(request, 'Accounts/register.html', args)
    elif request.method == 'GET' and request.user.is_authenticated == True:
        return redirect('/')
    elif request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        for user in users:
            if user.username == username:
                error += 2
        if password2 != password1:
            error += 1
        if error == 1:
            msg = "گذرواژه و تکرار گذرواژه یکسان نیستند"
            args = {'msg': msg, 'error': 1}
            return render(request, 'Accounts/register.html', args)
        elif error == 2:
            msg = "نام کاربری شما در سیستم موجود است"
            args = {'msg': msg, 'error': 1}
            return render(request, 'Accounts/register.html', args)
        elif error == 3:
            msg = "نام کاربری شما در سیستم موجود است گذرواژه و تکرار گذرواژه یکسان نیستند"
            args = {'msg': msg, 'error': 1}
            return render(request, 'Accounts/register.html', args)
        user = User(first_name=firstname, last_name=lastname, username=username, email=email)
        user.set_password(password1)
        user.save()
        lgn(request, user)

        return redirect('/')


def Login(request):
    arg = {'error': 0}
    if request.method == 'GET' and request.user.is_authenticated == False:
        return render(request, 'Accounts/login.html', arg)
    elif request.method == 'GET' and request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        i = authenticate(request, username=username, password=password)
        if i:
            lgn(request, i)
            return redirect('/')
        arg = {'error': 1}
        return render(request, 'Accounts/login.html', arg)


@login_required
def Logout(request):
    lgt(request)
    return redirect('/')


@login_required
def Profile(request):
    profile = request.user.ProfileModel
    return render(request, 'Accounts/profile.html', {'profile': profile.avatar})


@login_required
def EditProfile(request):
    profile = request.user.ProfileModel
    if request.method == "GET":
        return render(request, 'Accounts/editprofile.html', {'profile': profile})
    else:
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        avatar = request.FILES['myfile']
        profile.avatar = avatar
        profile.save()
        if fname != "":
            request.user.first_name = fname
        if lname != "":
            request.user.last_name = lname
        request.user.save()
        return redirect('/accounts/profile', {'profile': profile})


@login_required
def Panel(request):
    return render(request, 'Accounts/panel.html')


@login_required
def createcourse(request):
    if not request.user.is_superuser:
        return redirect('/accounts/panel')
    if request.method != "POST":
        return render(request, 'Accounts/createcourse.html')
    else:
        department = request.POST['department']
        name = request.POST['name']
        teacher = request.POST['teacher']
        groupnumber = request.POST['group_number']
        coursenumber = request.POST['course_number']
        starttime = request.POST['start_time']
        endtime = request.POST['end_time']
        firstday = request.POST['first_day']
        secondday = request.POST['second_day']
        course = Course(department=department, name=name, teacher=teacher, group_number=groupnumber,
                        course_number=coursenumber, start_time=starttime, end_time=endtime, first_day=firstday,
                        second_day=secondday)
        course.save()
        return redirect('/accounts/panel')


def add(request, pk):
    added = x(user=request.user, course=Course.objects.get(pk=pk))
    added.save()
    return redirect('/accounts/panel/courses')


def courses(request):
    mycourses = x.objects.filter(user=request.user)
    coursess = x.objects.filter(~Q(user=request.user))
    args = {'courses': coursess, 'mycourses': mycourses}
    if request.method == "POST":
        querysearch = request.POST['search_query']
        teacher = Course.objects.filter(teacher=querysearch)
        department = Course.objects.filter(department=querysearch)
        course = Course.objects.filter(name=querysearch)
        filteredCourses = []
        if request.POST.get('teacher'):
            filteredCourses += list(teacher)
        if request.POST.get('department'):
            filteredCourses += list(department)
        if request.POST.get('course'):
            filteredCourses += list(course)
        if not request.POST.get('course') and not request.POST.get('department') and not request.POST.get('teacher'):
            filteredCourses += list(department)
        filteredCourses = set(filteredCourses)
        args = {'courses': coursess, 'searchResults': filteredCourses, 'mycourses': mycourses}
        return render(request, 'Accounts/Courses.html', args)
    return render(request, 'Accounts/Courses.html', args)
