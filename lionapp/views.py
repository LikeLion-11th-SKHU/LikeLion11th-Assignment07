from django.shortcuts import render
from .models import Lion_Post
# Create your views here.

def main(request) :
    return render(request,'main.html')

def goeun(request) :
    return render(request,'goeun.html')

def main(request) :
    lion_posts = Lion_Post.objects.all
    return render(request,'main.html',{'lion_posts':lion_posts})

def goeun(request) :
    return render(request,'goeun.html',{'lion_post':Lion_Post.objects.all})
