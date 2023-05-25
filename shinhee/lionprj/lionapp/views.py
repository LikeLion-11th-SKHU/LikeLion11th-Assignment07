from django.shortcuts import render
from .models import Lion_Post
from .models import Ex_Post
# Create your views here.

def main(request):
    lion_post = Lion_Post.objects.all
    return render(request, 'main.html', {'lion_posts': lion_post})

def shinhee(request):
    ex_post = Ex_Post.objects.all()
    return render(request, 'shinhee.html', {'ex_post': ex_post})