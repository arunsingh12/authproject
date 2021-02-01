from django.contrib import admin
from django.urls import path,include
from WebApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home_page, ),
    path('customer/', views.Customer_page),
    path('regis/', views.Registration_page),
    path('logout/', views.Logout_page),
    path('accounts/',include('django.contrib.auth.urls')),

]
