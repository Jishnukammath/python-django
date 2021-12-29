from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method=='POST':
        user_name=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                print('acount created')
        else:
            messages.info(request, 'password  not matching')
            return redirect('register')
        return redirect('/')


    else:
     return render(request,'rejister.html')






def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'ivalid details')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

