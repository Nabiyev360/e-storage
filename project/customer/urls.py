from django.urls import path

from .views import *


app_name = 'customer'

urlpatterns = [
    path('', ProductsView, name='home'),
    path('products/', ProductsView, name='products'),
    path('details/<int:pk>/', ProductsDetailView, name='product-details'),
    path('details/', ProductsDetailView, name='product-details'),
    path('my-orders/', MyOrdersView, name='my-orders'),
]
