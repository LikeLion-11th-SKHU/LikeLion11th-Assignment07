from django.shortcuts import render
from .models import Ex_Post, Ex2_Post

# Create your views here.
def main(request):
    ex_posts = Ex_Post.objects.all
    return render(request, 'main.html', {'ex_posts' : ex_posts})

def dongjae(request):
    ex2_posts = Ex2_Post.objects.all
    return render(request, 'dongjae.html', {'ex2_posts' : ex2_posts})