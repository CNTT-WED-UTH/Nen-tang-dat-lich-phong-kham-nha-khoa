from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        # Lấy tên đăng nhập và mật khẩu từ form
        username = request.POST['username']
        password = request.POST['password']
        
        # Thực hiện xác thực người dùng
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Nếu người dùng hợp lệ, đăng nhập và chuyển hướng
            login(request, user)
            return redirect('home')  # Chuyển hướng đến trang chủ (có thể thay bằng URL khác)
        else:
            # Nếu không hợp lệ, hiển thị thông báo lỗi
            return render(request, 'app/login.html', {'error': 'Tên đăng nhập hoặc mật khẩu không đúng.'})
    
    # Nếu là yêu cầu GET, hiển thị form đăng nhập
    return render(request, 'app/login.html')
def home(request):
    return render(request, 'app/home.html')