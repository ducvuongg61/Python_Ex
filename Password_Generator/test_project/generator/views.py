from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return HttpResponse("Hello World!")

def eggs(request):
    return HttpResponse("<h1>Eggs!! Checkout</h1>")

def newHome(request):
    return render(request, 'generator/home.html' , {'password' : 'ajkaldksjl'})

def password(request):
    thepassword = ''
    characters = list('abcdefghiklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('()!@#$^&*/+-~`|/'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
   

    lenght = int(request.GET.get('length'))
    
    for x in range(lenght) :
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html' , {'password' :  thepassword})