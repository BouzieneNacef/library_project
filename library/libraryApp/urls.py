from django.urls import path
from. import views

urlpatterns=[
    path("", views.ahla, name='ahla'),
    path("home/", views.home, name='home'),
    
   
]