from django.http import HttpResponse
from django.shortcuts import render
from .models import Products

# Create your views here.

#/products -> index
#url-uniform resource locator-address


def index(request):
    products = Products.objects.all()
    return render(request, 'index.html',
                  {'products':products})


def new(request):
    return HttpResponse('New products available')
