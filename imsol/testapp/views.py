from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'imsol.html')

def index(request):
    return render(request,'main.html')