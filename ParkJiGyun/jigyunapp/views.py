from django.shortcuts import render
from .models import Jigyun_Post

# Create your views here.

def main(request):
    return render(request, 'main.html')

def Jigyun(request):
    return render(request,'Jigyun.html')

def main(request):
    jigyun_posts = Jigyun_Post.objects.all
    print(jigyun_posts)
    return render(request, 'main.html', {'jigyun_posts': jigyun_posts})

def Jigyun(request):
    jigyun_posts = Jigyun_Post.objects.all
    return render(request, 'Jigyun.html', {'jigyun_posts': jigyun_posts})