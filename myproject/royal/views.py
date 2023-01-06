from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib import auth


# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            message.info(request,"invalid royal")
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        newpassword = request.POST['password1']
        if password == newpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

