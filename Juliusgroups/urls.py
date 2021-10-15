
from os import name
from django.contrib.auth import logout
from django.urls import path
from Juliusgroups.views import home_view,loginpage,registrationform, logoutUser,contact,Thankyoupage


urlpatterns = [
    path('',home_view, name="home"),
    path('login/',loginpage, name="login"),
    path('logout/',logoutUser, name="logout"),
    path('contact/', contact, name="Contact"),
    path('register/', registrationform, name = "register"),
    path('thankyou/', Thankyoupage, name = "thankyou"),

   
    
]
