from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('dashpage/',dashpage),
    path('find_doctor/',find_doctors),
    path('consults/',consult),
    path('medicine/',medical),
    path('labs/',lab),
    path('surgeries/',surgrey),
    path('tips/',tip),
    path('more/',more),
    path('login/',logsing),
    path('appointment/',appointment),
    path('appointment/history/',history),
    path('appointment/history/delete/<int:id>/',Delete,name='appointment_delete'),
    path('appointment/history/update/<int:id>/',Update,name='appointment_update'),
    
  


     path('abouts/', about),
     path('contact/', contact),
     path('career/', careers),
     path('apply/', apply),
     path('FAQ/', faqs),
     path('privacy/', privacy),
     path('terms/', term),

    #  doctors_about

    path('sai/',drsai),
    path('naresh/',drnaresh),
    path('shilpa/',shilpa),
    path('ravinder/',ravinder),
    path('jeeson/',jeeson),
    path('aravind/',aravind),
    path('mani/',mani),
    path('asha/',asha),
    path('aswathy/',aswathy),
    path('bhawna/',bhawna),
    path('vinod/',vinod),
    path('randhir/',randhir),


    
]