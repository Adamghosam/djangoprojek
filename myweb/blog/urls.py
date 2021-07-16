from django.urls import path
from . import views

# url 
urlpatterns=[
    path('artikel/',views.home),
    path('',views.index),

]