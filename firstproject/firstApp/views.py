from django.http import HttpResponse
from django.shortcuts import render
from .models import Destination,News

# Create your views here.
def fun(request):
    obj=Destination.objects.all()
    obj1=News.objects.all()
    return render(request,'index.html',{'results': obj,'result1':obj1})

# def addition(request):
#     num1=int(request.POST['num1'])
#     num2 = int(request.POST['num2'])
#     result=num1+num2
#     return render(request,"result.html",{'result':result})
