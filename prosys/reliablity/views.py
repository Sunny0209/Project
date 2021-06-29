from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def home(request):
    return render(request,'index.html')

def predictor(request):
    return render(request,'upload.html')

def result(request):
    return render(request,'result.html')