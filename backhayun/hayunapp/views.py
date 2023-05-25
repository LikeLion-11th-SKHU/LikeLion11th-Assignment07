from django.shortcuts import render
from .models import Hayun_Post
# Create your views here.

def main(request):
    return render(request, 'main.html')

def hayun(request):
    return render(request, 'hayun.html')

def main(request):
    hayun_posts = Hayun_Post.objects.all
    return render(request, 'main.html', {'hayun_posts': hayun_posts})

def hayun(request):
    return render(request, 'hayun.html', {'hayun_post': Hayun_Post.objects.all})