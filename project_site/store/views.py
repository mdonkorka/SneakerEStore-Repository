from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def homepage(request):
    
    context = {}
    return render(request, 'store/homepage.html', context)

# Create your views here.
def store(request):
    
    context = {}
    return render(request, 'store/store.html', context)

def about(request):
    
    context = {}
    return render(request, 'store/about.html', context)

def cart(request):
    
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    
    context = {}
    return render(request, 'store/checkout.html', context)