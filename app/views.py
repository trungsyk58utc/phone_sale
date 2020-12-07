from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
priceList = [
    {'id':1, 'name':'Dưới 5 triệu', 'max':5},
    {'id':2, 'name':'Từ 5 đến 10 triệu','min':5, 'max':10},
    {'id':3, 'name':'Từ 10 đến 20 triệu','min':10, 'max':20},
    {'id':4, 'name':'Trên 20 triệu','min':20},
]

def index(request):
    name = request.GET.get('name','')
    categoryId = request.GET.get('categoryId')
    categoryList = Category.objects.all()
    productList = Product.objects.filter(name__icontains=name)
    ramList = RAM.objects.all()
    ramId = request.GET.get('ramId')
    romList = ROM.objects.all()
    romId = request.GET.get('romId')
    
    priceId = request.GET.get('priceId')
    priceId = int(priceId) if priceId else None
    price = priceList[priceId-1] if priceId else {}
    minPrice, maxPrice = price.get('min'), price.get('max')

    categoryId = int(categoryId) if categoryId else None
    if categoryId:
        productList = productList.filter(category__id=categoryId)
    
    ramId = int(ramId) if ramId else None
    if ramId:
        productList = productList.filter(ram__id=ramId)

    romId = int(romId) if romId else None
    if romId:
        productList = productList.filter(rom__id=romId)
    
    if minPrice: 
        productList = productList.filter(price__gte=minPrice)

    if maxPrice:
        productList = productList.filter(price__lte=maxPrice)
    context = {
        'productList':productList,
        'categoryList':categoryList,
        'categoryId':categoryId,
        'name':name,
        'ramList':ramList,
        'romList':romList,
        'ramId':ramId,
        'romId':romId,
        'priceId':priceId,
        'priceList':priceList,
    }
    return render(request, 'user/index.html', context)

def viewProduct(request,pk):
    product = Product.objects.get(pk=pk)
    context = {'product':product}
    return render(request, 'user/product.html', context)

def orderProducts(request, pk):
    product = Product.objects.get(pk=pk)
    form = OrderForm()
    
    if request.method == 'POST':
        form = OrderForm(request.POST) 

        if form.is_valid():
            request.session['order_form'] = form.cleaned_data
            return redirect('confirm-order', pk)

    context = {'product':product, 'form':form}
    return render(request, 'user/order.html', context) 

def confirmOrder(request, pk):
    product = Product.objects.get(pk=pk)
    form = request.session.get('order_form')
    context = {'form':form, 'product':product}
    return render(request, 'user/confirm-order.html', context)


def thankYou(request, pk):
    product = Product.objects.get(pk=pk)
    form = request.session.get('order_form')

    Order.objects.create(
        product = product,
        fullname = form['fullname'],
        phone=form['phone'],
        address=form['address'],
        order_date=datetime.now(),
        status=Order.Status.NEW
    )
    return render(request, 'user/thankyou.html')

def signup(request):
    form = UserCreationForm()
   
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                    password=request.POST['password1'])
            login(request, user)
            return redirect('home')
    
    return render(request, 'registration/signup.html', {'form':form})
