from django.http import HttpResponse
from django.shortcuts import render,redirect

# from first.forms import modelForm
from .forms import modeForm
from .models import shop
# Create your views here.

def demo(request):
    product=shop.objects.all()
    return render(request,'home.html',{'products':product})



def details(request,shop_id):
    product1=shop.objects.get(id=shop_id)
    return render(request,'details.html',{'product':product1})


def add_product(request):
    if request.method =='POST':
        name=request.POST.get('name')
        disc=request.POST.get('disc')
        price=request.POST.get('price')
        img=request.FILES['img']
        s=shop(name=name,disc=disc,img=img,price=price)
        s.save()
    return render(request,'add_product.html')


def edit(request,id):
    obj=shop.objects.get(id=id)
    form=modeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})




def delete(request,id):
    if request.method == 'POST' :
        obj=shop.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')
