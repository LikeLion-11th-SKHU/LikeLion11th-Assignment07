from django.shortcuts import render
# from .models import Lion_Post
from .models import Ex_Post
from .models import Nowon
from .models import Position

# Create your views here.
# def main(request):
#     lion_posts = Lion_Post.objects.all
#     return render(request, 'main.html', {'lion_posts': lion_posts})

def main(request):
    ex_posts = Ex_Post.objects.all
    nowon = Nowon.objects.all
    return render(request, 'main.html', {'ex_posts': ex_posts, 'nowon': nowon})

def Jungdaun(request):
    ex_posts = Ex_Post.objects.all
    positions = Position.objects.all
    return render(request, 'Jungdaun.html', {'ex_posts': ex_posts, 'positions': positions})
