from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields={'slug':('category_name',)}
  list_display=('category_name','slug','created_at','updated_at')
  list_display_links=('category_name','slug')
  readonly_fields=('created_at','updated_at')
  
# Register your models here.
admin.site.register(Category,CategoryAdmin)
