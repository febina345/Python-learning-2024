from django.urls import path
from . import views


#/products
#products/1/details
#products
urlpatterns = [
    path('',views.index),
    path('new/',views.new)
]