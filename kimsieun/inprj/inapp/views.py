from django.shortcuts import render
from .models import Ex_Post
from .models import Si_Post
# Create your views here.

def main(request):
    ex_posts = Ex_Post.objects.all
    return render(request, 'main.html', {'ex_posts': ex_posts})

def sieun(request):
    si_posts = Si_Post.objects.all
    return render(request, 'sieun.html', {'si_posts': si_posts})

