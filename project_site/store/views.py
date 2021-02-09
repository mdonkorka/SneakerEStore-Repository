from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from .models import *  




def homepage(request):
    
    context = {}
    return render(request, 'store/homepage.html', context)

# Create your views here.
def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)

def about(request):
    
    context = {}
    return render(request, 'store/about.html', context)

def cart(request):
    

    if request.user.is_authenticated:
	    customer = request.user.customer
	    order, created = Order.objects.get_or_create(customer=customer, complete=False)
	    items = order.orderitem_set.all()
    else:
	    #Create empty cart for now for non-logged in user
	    items = []
	    order = {'get_cart_total':0, 'get_cart_items':0}


    context = {'items' :items, 'order' :order}
    return render(request, 'store/cart.html', context)

    

def checkout(request):


    if request.user.is_authenticated:
	    customer = request.user.customer
	    order, created = Order.objects.get_or_create(customer=customer, complete=False)
	    items = order.orderitem_set.all()
    else:
	    #Create empty cart for now for non-logged in user
	    items = []
	    order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items' :items, 'order' :order}
    return render(request, 'store/checkout.html', context)


    
    context = {}
    return render(request, 'store/checkout.html', context)