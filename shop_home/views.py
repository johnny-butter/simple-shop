from django.shortcuts import render
from api.models import Product, Order


def home(request):
    if request.method == 'GET':
        products = Product.objects.all()
        orders = Order.objects.filter(customer_id=1)

        return render(request, 'home.html', locals())
