from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def index(request):
    
    context = {}
    return render(request, 'store/index.html', context)

# Create your views here.
def aboutPage(request):
    
    context = {}
    return render(request, 'store/about.html', context)