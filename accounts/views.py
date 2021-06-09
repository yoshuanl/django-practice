from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    orderList = Order.objects.all()
    customerList = Customer.objects.all()

    totalOrder = orderList.count()
    totalCustomer = customerList.count()
    delivered = orderList.filter(status='Delivered').count()
    pending = orderList.filter(status='Pending').count()

    data = {
        'orderList': orderList, 
        'customerList': customerList,
        'totalOrder': totalOrder,
        'totalCustomer': totalCustomer,
        'delivered': delivered,
        'pending': pending
        }

    return render(request, 'accounts/dashboard.html', data)

def products(request):
    productList = Product.objects.all()

    data = {'productList': productList}

    return render(request, 'accounts/products.html', data)

def customer(request):
    return render(request, 'accounts/customer.html')
