from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'polls/home.html')

def orden(request):
    return render(request,'polls/orden.html')