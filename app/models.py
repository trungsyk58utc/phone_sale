from django.db import models

# Create your models here.

class ROM(models.Model):
    value_rom = models.CharField(max_length=10, unique=True, verbose_name='Bộ nhớ')
    def __str__(self):
        return self.value_rom

class RAM(models.Model):
    value_ram = models.CharField(max_length=10, unique=True, verbose_name='RAM')
    def __str__(self):
        return self.value_ram

class Category(models.Model):
    code = models.CharField(max_length=255, unique=True, verbose_name='Mã')
    name = models.CharField(max_length=255, verbose_name='Tên')
    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=255, unique=True, verbose_name= 'Mã')
    name = models.CharField(max_length=255, verbose_name='Tên')
    ram = models.ForeignKey(RAM, verbose_name='RAM', on_delete = models.PROTECT)
    rom = models.ForeignKey(ROM, verbose_name='Bộ nhớ', on_delete = models.PROTECT)
    price = models.FloatField(verbose_name = 'Giá', null=True)
    description = models.CharField(max_length=255, verbose_name='Mô tả', blank=True)
    category = models.ForeignKey(Category, verbose_name='Nhãn hiệu', on_delete = models.PROTECT)
    image = models.ImageField(verbose_name='ảnh', upload_to = 'static/image')
    def __str__(self):
        return self.name

class Order(models.Model):
    class Status:
        NEW = 0
        DELIVERED = 1
        CANCELED = 2
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(null=True)
    status = models.IntegerField()
