from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home,),
    #path('index/',views.home,name="home"),
    #path('signup/',views.signup, name="signup"),
    #path('login/',views.login_user, name="login"),
    #path('signout/',views.signout, name="signout"),
    #path('drive_or_ride/',views.driveorride,name="drive_or_ride"),
    path('Driver/',views.Driver,name="Driver"),
   # path('driver_dashboard/',views.driver_dashboard,name="driver_dashboard"),
    
]