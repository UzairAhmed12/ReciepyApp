from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    peoples = [
        {'name' : 'Uzair', 'age':22},
        {'name' : 'Ali', 'age':23},
        {'name' : 'hamza', 'age':24},
        {'name' : 'nasir', 'age':25},
        {'name' : 'saif', 'age':26},
    ]
    return render(request , "home/index.html", context = {'peoples':peoples})

def about(request):
        return render(request, "home/about.html")


def contact(request):
        return render(request, "home/contact.html")