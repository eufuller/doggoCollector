from django.shortcuts import render
from .models import Dog


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/doggoIndex.html', {'dogs': dogs})

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/doggoIndex.html', {'dogs': dogs})