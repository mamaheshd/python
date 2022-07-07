from re import template
from django.shortcuts import render
from django.shortcuts import render,redirect
from book.models import Laptops
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
def index(request):
    #print(request.user)
    laptop_list=Laptops.objects.all()
    laptops={
        'laptops':laptop_list #key value side
    }
    return render(request,'book/Laptop-list.html',laptops)

@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
def delete(request,id):
	del_obj=Laptops.objects.get(id=id)
	del_obj.delete()
	return redirect('index')

@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
def create(request):
    if request.method == "POST":
        model = request.POST['model']
        manufacturer = request.POST['manufacturer']
        cpu = request.POST['cpu']
        gpu = request.POST['gpu']
        ram = request.POST['ram']
        price = request.POST['price']
        laptop = Laptops(name=model,manufacturer=manufacturer,cpu=cpu,gpu=gpu,ram=ram,price=price)
        laptop.save()
        return redirect('index')
    else:
        return render(request, 'book/laptop-create.htm')

#update

@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
def update(request, id):
    obj = Laptops.objects.get(id=id)
    queryset={
    'queryset':obj  
    }
    if request.method == "POST":
        model = request.POST['model']
        manufacturer = request.POST['manufacturer']
        cpu = request.POST['cpu']
        gpu = request.POST['gpu']
        ram = request.POST['ram']
        price = request.POST['price']

        obj.name=model
        obj.manufacturer=manufacturer
        obj.cpu=cpu
        obj.gpu=gpu
        obj.ram=ram
        obj.price=price
        obj.save()
        return redirect('index')
    else:
        return render(request,'book/laptop-update.htm', queryset)