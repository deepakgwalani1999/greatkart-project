from django.urls import path
from .views import store
from .views import product_details

urlpatterns=[
  path('',store,name='store'),
  path('<slug:slug>/',store,name='category_by_slug'),
  path('<slug:slug>/<slug:product_slug>/',product_details,name='products_by_slug'),
  
]

