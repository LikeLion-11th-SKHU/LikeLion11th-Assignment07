from django.shortcuts import render
from .models import Ex_Post, Backend


# Create your views here.


def main(request):
    ex_posts = Ex_Post.objects.all
    return render(request, "main.html", {"ex_posts": ex_posts})


def junyeong(request):
    backend = Backend.objects.all
    return render(request, "junyeong.html", {"backend": backend})
