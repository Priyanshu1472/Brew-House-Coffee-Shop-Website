from django.contrib import admin
from django.urls import path
from test1 import views

urlpatterns = [
    path('',views.index,name="home"),
    path('navbar',views.navbar,name='navbar'),
    path('footer',views.footer,name='footer'),
    path('menu',views.Menu,name='menu'),
    path('about',views.about,name='about'),
    path('cookies',views.cookies,name='cookies'),
    path('beverages',views.beverages,name='beverages'),
    path('sweets',views.sweets,name='sweets'),
    path('desserts',views.desserts,name='desserts'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('cart',views.mycart,name='cart'),
    path('feedback',views.fb,name='feedback'),
    path('checkout',views.checkout,name='checkout'),
    path('popup',views.popup,name='popup'),
    path('fav',views.fav,name='fav')
]