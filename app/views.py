from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context= {}
    return render(request,'app/home.html')
def cart(request):
    context= {}
    return render(request,'app/cart.html',context)
def checkout(request):
    context= {}
    return render(request,'app/checkout.html',context)
def gioithieu(request):
    context= {}
    return render(request,'app/gioithieu.html',context)
def dichvu(request):
    context= {}
    return render(request,'app/dichvu.html',context)
def banggia(request):
    context= {}
    return render(request,'app/banggia.html',context)
def tintuc(request):
    context= {}
    return render(request,'app/tintuc.html',context)