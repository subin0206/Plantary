from django.shortcuts import render, get_object_or_404
from .models import Product
from account.models import Profile
# Create your views here.

def storemain(request):
    products = Product.objects
    profile = Profile.objects.all()
    current_user = request.user
    return render(request, 'store.html', {'products':products, 'profile':profile, 'current_user':current_user})

def storemanager(request):
    products = Product.objects
    return render(request, 'storemanager.html', {'products':products})    

def registerproduct(request):
    return render(request, 'registerproduct.html')

def productdetail(request, product_id):
    product_detail = get_object_or_404(Product, pk=product_id)
    profile = Profile.objects.all()
    current_user = request.user
    return render(request, 'productdetail.html', {'product':product_detail,'profile':profile, 'current_user':current_user})