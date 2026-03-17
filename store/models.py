from django.db import models
from category.models import Category
from django.urls import reverse
class Product(models.Model):
  product_name=models.CharField(max_length=200,unique=True)
  product_slug=models.SlugField(max_length=200,unique=True)
  description=models.TextField(max_length=500,blank=True)
  price=models.IntegerField()
  product_image=models.ImageField(upload_to="photos/products")
  stock=models.IntegerField()
  is_available=models.BooleanField(default=True)
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  
  def get_absolute_url(self):
    return reverse('products_by_slug',args=[self.category.slug,self.product_slug])
  
  def __str__(self):
    return self.product_name
  
    
  
  
# Create your models here.
