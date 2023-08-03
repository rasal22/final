from django.http import HttpResponse
from django.shortcuts import render
from .models import features
from . models import courses
from . models import trainers
from . models import products



# Create your views here.
def index(request):
    obj = features.objects.all()
    object = courses.objects.all()
    ob=trainers.objects.all()
    ob1=products.objects.all()

    return render(request, "index.html", {'result': obj,'resultt':object,'res':ob,'res1':ob1})

def about(request):
    return render(request,'about.html')

def computer(request):

    return render(request,"computer.html")

def commerce(request):

    return render(request,"commerce.html")

def science(request):
    return render(request,"science.html")

def philosophy(request):
    return render(request,"philosophy.html")

def psychology(request):
    return render(request,"psychology.html")