from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('boc-rang-su.html/', views.boc_rang_su, name="boc_rang_su"),

]