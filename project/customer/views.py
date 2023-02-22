from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from storage.models import Customer, Product, Order, OrderItem


@login_required
def ProductsView(request):
    customer = Customer.objects.get(user=request.user)
    products = Product.objects.all()

    ctx = {
        'fullname': customer.name,
        'products': products
    }

    return render(request, "customer/store/product-card.html", ctx)


@login_required
def ProductsDetailView(request, pk):
    customer = Customer.objects.get(user=request.user)
    product = Product.objects.get(id=pk)

    ctx = {
        'fullname': customer.name,
        'product': product
    }

    if request.method == 'GET':
        return render(request, "customer/store/product-details.html", ctx)

    elif request.method == 'POST':
        quantity = request.POST['count']

        order = Order(customer=customer, status='Navbatda')
        order.save()

        item = OrderItem(product=product, order=order, quantity=quantity)
        item.save()


        orders = Order.objects.filter(customer=customer)
        order_dict = {}

        for order in orders:
            order_dict[order] = OrderItem.objects.filter(order=order).first()

        ctx = {
            'fullname': customer.name,
            'order_dict': order_dict,
            'orders': orders,
        }
        return render(request, "customer/store/my-orders.html", ctx)



@login_required
def MyOrdersView(request):
    customer = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(customer=customer)
    order_dict = {}

    for order in orders:
        order_dict[order] = OrderItem.objects.filter(order=order).first()

    ctx = {
        'fullname': customer.name,
        'order_dict': order_dict,
        'orders': orders,
    }

    return render(request, "customer/store/my-orders.html", ctx)
