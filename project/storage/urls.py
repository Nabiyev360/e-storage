from django.urls import path

from .views import *


app_name = 'storage'

urlpatterns = [
    path('', HomeView, name='home'),
    path('stats/', HomeView, name='stats'),
    path('orders/', OrdersView, name='orders'),
    path('products/', products_view, name='products'),
    path('customers/', CustomersView, name='customers'),
    path('customer-details/', CustomerDetailsView, name='customer-details'),
    path('supports/', SupportView, name='supports'),
    path('settings/', SettingsView, name='settings'),
    path('ingetration/', Integrations, name='integration'),
    path('user-profile/', UserProfile, name='user-profile'),

    path('delete-product/<int:id>', delete_product_view, name='delete-product')
]