from django.urls import path
from .views import *

urlpatterns=[
    path('',loginpage),
    path('signup/',signup,name='signup'),
    path('logout/',logoutuser)
]