from django.urls import path
from. import views

urlpatterns=[
    path("",views.home),
    path("book/",views.book),
    path("about/",views.about)
]