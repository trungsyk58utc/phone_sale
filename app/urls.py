from django.urls import path, include
from .views import *
from .views_staff import *

urlpatterns = [
    # trang dành cho người dùng
    path('', index, name='home'),
    path('view-product/<pk>', viewProduct, name='view-product'),
    path('order-product/<pk>', orderProducts, name='order-product'),
    path('thankyou/<pk>', thankYou, name='thankyou'),
    path('confirm-order/<pk>', confirmOrder, name='confirm-order'),
    # trang đăng nhập dành cho quản trị viên
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', signup),
    # trang chỉnh sửa nhãn hàng
    path('staff/', listCategories, name='list-categories'),
    path('staff/categories-create', CategoriesCreateView.as_view(), name = 'categories-create'),
    path('staff/categories-update/<pk>', CategoriesUpdateView.as_view(), name = 'categories-update'),
    path('staff/categories-delete/<pk>', deleteCategories, name = 'categories-delete'),
    # trang chỉnh sửa sản phẩm
    path('staff/list-product', listProducts, name='list-product'),
    path('staff/product-create', ProductCreateView.as_view(), name='product-create'),
    path('staff/product-update/<pk>', ProductUpdateView.as_view(), name='product-update'),
    path('staff/product-delete/<pk>', deleteProduct, name='product-delete'),
    # trang thông tin đặt hàng
    path('staff/list-order', listOrderProducts, name='list-order-product'),
    path('staff/delivery-order/<pk>', deliveryOrder, name='delivery-order'),
    path('staff/cancel-order/<pk>', cancelOrder, name='cancel-order'),
]