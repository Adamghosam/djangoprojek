from django.shortcuts import render
from . import models
import datetime


# Create your views here.

def index (request):
    
    now = datetime.datetime.now()
    posting = models.Posting.objects.all()
    context={
        'title':'Home',
        'Nama':'Adam ghosam',
        'post':posting,
        'time':now
    }

    return render (request,'blog/index.html',context)

def home(request):

    return render(request,'blog/artikel.html')


def tutorial(request):

    return render(request,'blog/tutorial.html')


def about(request):

    return render(request,'blog/about.html')

