from django.urls import path
from . import views

# url 
urlpatterns=[
    path('tutorial/',views.tutorial),
    path('about/',views.about),
    path('artikel/',views.home),
    path('',views.index),

]