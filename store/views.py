from django.shortcuts import render
from .models import Product
from category.models import Category
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
def store(request,slug=None):
  
  
  if slug:
    category=get_object_or_404(Category,slug=slug)
    products=Product.objects.filter(category=category,is_available=True)
   
  else:
    products=Product.objects.all().filter(is_available=True)
  product_count=products.count()  
  # products=Product.objects.all().filter(is_available=True)
  context={'products':products,'product_count':product_count}
  return render(request,'store/store.html',context)
def product_details(request,slug,product_slug):
  try:
    single_product=Product.objects.get(category__slug=slug,product_slug=product_slug)
  except Exception as e:
    print("==============>",e)
    return e
  context={'single_product':single_product}
  return render(request,'store/product_details.html',context)



    

# Create your views here.
