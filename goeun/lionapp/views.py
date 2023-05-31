from django.shortcuts import render
from .models import Lion_Post,Lion_Post02
# Create your views here.
def main(request) :
    lion_posts = Lion_Post.objects.all
    return render(request,'main.html',{'lion_posts':lion_posts})

def goeun(request) :
    lion_post = Lion_Post02.objects.all
    return render(request,'goeun.html',{'lion_post':lion_post})