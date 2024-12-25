from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('gioithieu/', views.gioithieu, name="gioithieu"),
    path('dichvu/', views.dichvu, name="dichvu"),
    path('banggia/', views.banggia, name="banggia"),
    path('tintuc/', views.tintuc, name="tintuc"),
    path('datlich/', views.datlich, name="datlich"),
]