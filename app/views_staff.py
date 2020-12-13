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
def listRom(request):
    romList = ROM.objects.all()
    return render(request, 'staff/Rom/list.html', {'romList': romList})

@method_decorator(login_required, name='dispatch')
class RomUpdateView(UpdateView):
    model = ROM
    fields = '__all__'
    template_name = 'staff/Rom/form.html'
    success_url = '/staff/list-rom'

@method_decorator(login_required, name='dispatch')
class RomCreateView(CreateView):
    model = ROM
    fields = '__all__'
    template_name = 'staff/Rom/form.html'
    success_url = '/staff/list-rom'

@login_required
def deleteRom(request, pk):
    rom = ROM.objects.get(pk=pk)
    rom.delete()
    return redirect('list-rom')

@login_required
def listRam(request):
    ramList = RAM.objects.all()
    return render(request, 'staff/ram/list.html', {'ramList': ramList})

@method_decorator(login_required, name='dispatch')
class RamCreateView(CreateView):
    model = RAM
    fields = '__all__'
    template_name = 'staff/ram/form.html'
    success_url = '/staff/list-ram'

@method_decorator(login_required, name='dispatch')
class RamUpdateView(UpdateView):
    model = RAM
    fields = '__all__'
    template_name = 'staff/ram/form.html'
    success_url = '/staff/list-ram'

@login_required
def deleteRam(request, pk):
    ram = RAM.objects.get(pk=pk)
    ram.delete()
    return redirect('list-ram')

@login_required
def listOrderProducts(request):
    listOrder = Order.objects.all().order_by('status')
    return render(request, 'staff/order/list.html', {'listOrder':listOrder})

@login_required 
def deliveryOrder(request, pk):
    delivery_date_error = ''
    if request.method == 'POST':
        try:
            delivery_date = datetime.strptime(request.POST['delivery_date'], '%d/%m/%Y %H:%M')
        except:
            delivery_date_error = 'Thời gian không hợp lệ'
        
        if delivery_date_error == '':
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


