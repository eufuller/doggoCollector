from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>About</h1>')
    # return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/doggoIndex.html', {'dogs': dogs})

class Dog:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Lolo', 'tabby', 'foul little demon', 3),
    Dog('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Dog('Raven', 'black tripod', '3 legged Dog', 4)
]