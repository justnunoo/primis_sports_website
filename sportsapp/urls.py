from django.urls import path, include
from . import views

urlpatterns =[
    path("", views.index, name= "index"), # index page
    path("register_trainee/", views.register_trainee, name= "register_trainee")
]