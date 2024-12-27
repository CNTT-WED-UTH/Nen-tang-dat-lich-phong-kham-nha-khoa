from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    services= Service.objects.all()
    context= {'services': services}
    return render(request, 'app/home.html',context)
def cart(request):
    context= {}
    return render(request, 'app/cart.html',context)
def checkout(request):
    context= {}
    return render(request, 'app/checkout.html',context)
def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Kiểm tra mật khẩu và xác nhận mật khẩu
        if password != confirm_password:
            messages.error(request, 'Mật khẩu và xác nhận mật khẩu không khớp!')
            return redirect('register')

        # Tạo người dùng mới
        user = User.objects.create_user(username=email, password=password, email=email)
        user.first_name = full_name
        user.save()

        messages.success(request, 'Đăng ký thành công!')
        return redirect('login')  # Chuyển hướng đến trang đăng nhập sau khi đăng ký
    return render(request, 'app/register.html')
def login(request):
    return render(request, 'app/login.html')
def boc_rang_su(request):
    return render(request, 'app/boc-rang-su.html')
