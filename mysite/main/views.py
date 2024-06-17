from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello KiKi!</h1>")

def add(request):
    return HttpResponse("<h1>Add Task</h1>")
