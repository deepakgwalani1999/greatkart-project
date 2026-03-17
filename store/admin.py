from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
  list_display=('product_name','product_slug','price','stock','category','updated_at','created_at','is_available')
  prepopulated_fields={'product_slug':('product_name',)}
  list_display_links=('product_name','product_slug')
  list_editable=('is_available','price','stock',)
  readonly_fields=('created_at','updated_at')
  
  
# Register your models here.

admin.site.register(Product,ProductAdmin)