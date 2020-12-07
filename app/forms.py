#app/forms.py
from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class OrderForm(forms.Form):
    fullname = forms.CharField(label='Họ và tên')
    phone = forms.CharField(label='Số điện thoại')
    address = forms.CharField(label='Địa chỉ')