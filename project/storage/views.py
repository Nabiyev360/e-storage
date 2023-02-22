from django.shortcuts import render, redirect

from .decorators import logged_staff_only
from .models import Customer, Order, OrderItem, Product, ProductCategory

@logged_staff_only
def HomeView(request):
    return render(request, 'storage/dashboard/index.html')


@logged_staff_only
def OrdersView(request):
    orders = Order.objects.all()
    order_dict = {}

    for order in orders:
        order_dict[order] = OrderItem.objects.filter(order=order).first()

    ctx = {
        'orders':orders,
        'order_dict':order_dict
    }
    return render(request, "storage/dashboard/orders.html", ctx)


@logged_staff_only
def CustomersView(request):
    staffs = Customer.objects.all()
    ctx = {
        'staffs': staffs
    }
    return render(request, "storage/dashboard/customers.html", ctx)


@logged_staff_only
def CustomerDetailsView(request):
    return render(request, "storage/dashboard/customer-details.html")


@logged_staff_only
def SupportView(request):
    return render(request, "storage/dashboard/supports.html")


@logged_staff_only
def SettingsView(request):
        return render(request, "storage/dashboard/settings.html")


@logged_staff_only
def Integrations(request):
        return render(request, "storage/dashboard/integration.html")


@logged_staff_only
def UserProfile(request):
        return render(request, "storage/dashboard/user-profile.html")


# Products
@logged_staff_only
def products_view(request):
    if request.method == 'POST':
        new_product = Product(
            name = request.POST['name'],
            category=ProductCategory.objects.get(name=request.POST['category']),
            price = request.POST['price'],
            # sale_price = request.POST['sale_price'],
            # stock = request.POST['stock'],
            # sku = request.POST['sku'],
            # info = request.POST['info']
        )
        new_product.save()

    products = Product.objects.all()
    ctx = {
        'products':products
    }

    if request.session.get('alert'):
        ctx['alert']=True
        request.session['alert'] = False
    return render(request, "storage/dashboard/products.html", ctx)


@logged_staff_only
def delete_product_view(request, id):
    request.build_absolute_uri()
    product = Product.objects.filter(id=id).first()
    if product:
        # product.delete()
        request.session['alert'] = True

    return redirect(to='/products/', request=request)