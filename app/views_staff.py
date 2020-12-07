from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .views import *
from .forms import *
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator

@login_required
def listCategories(request):
    category = Category.objects.all()
    context = {'category':category}
    return render(request, 'staff/category/list.html', context)

@method_decorator(login_required, name='dispatch')
class CategoriesCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'staff/category/form.html'
    success_url = '/staff'

@method_decorator(login_required, name='dispatch')
class CategoriesUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'staff/category/form.html'
    success_url = '/staff'

@login_required
def deleteCategories(request, pk):
    c = Category.objects.get(pk=pk)
    c.delete()
    return redirect('list-categories')

@login_required
def listProducts(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'staff/product/list.html', context)

@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'staff/product/form.html'
    success_url = '/staff/list-product'

@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'staff/product/form.html'
    success_url = '/staff/list-product'

@login_required
def deleteProduct(request, pk):
    p = Product.objects.get(pk=pk)
    p.delete()
    return redirect('list-product')

@login_required
def listOrderProducts(request):
    listOrder = Order.objects.all().order_by('status')
    return render(request, 'staff/order/list.html', {'listOrder':listOrder})

@login_required 
def deliveryOrder(request, pk):
    deliverDate_error = ''
    if request.method == 'POST':
        try:
            delivery_date = datetime.strptime(request.POST['delivery_date'], '%d/%m/%Y %H:%M')
        except:
            delivery_date_error = 'Thời gian không hợp lệ'
        
        if deliverDate_error == '':
            order = Order.objects.get(pk=pk)
            order.status = Order.Status.DELIVERED
            order.delivery_date = delivery_date
            order.save()
            return redirect('list-order-product')
    
    return render(request, 'staff/order/form.html', {'delivery_date_error' : delivery_date_error})

@login_required 
def cancelOrder(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = Order.Status.CANCELED
    order.save()
    return redirect('list-order-product')


