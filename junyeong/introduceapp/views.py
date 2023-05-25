from django.shortcuts import render
from .models import Ex_Post

# Create your views here.


def main(request):
    ex_posts = Ex_Post.objects.all
    return render(request, "main.html", {"ex_posts": ex_posts})


def junyeong(request):
    return render(request, "junyeong.html", {"ex_posts": ex_posts})
