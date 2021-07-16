from django.shortcuts import render

# Create your views here.

def index (request):
    context={
        'title':'Home',
        'Nama':'Adam ghosam'
    }

    return render (request,'blog/index.html',context)

def home(request):

    return render(request,'blog/artikel.html')

