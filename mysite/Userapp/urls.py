from Userapp import views
#from django.contrib import admin
from django.urls import path,include
urlpatterns = [
   #path('',views.home,name='homes'),
    path('register/', views.register, name="register"),
    path('login/',views.user_login,name='user_login'),
    path('login/',views.user_logout,name='user_logout'),
    path("password_reset/",views.password_reset_request,name='password_reset')
]