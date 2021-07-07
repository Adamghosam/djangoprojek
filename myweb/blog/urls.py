from django.urls import path
from . import views

# url 
urlpatterns=[
    path('home/',views.home),
    path('',views.index),

]