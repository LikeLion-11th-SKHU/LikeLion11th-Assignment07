from django.shortcuts import render
from .models import Lion_Post, Position, Hometown

# Create your views here.

def main(request):
    lion_posts = Lion_Post.objects.all
    hometowns = Hometown.objects.all
    return render(request, 'main.html', {'lion_posts':lion_posts, 'hometowns': hometowns})

def gaeul(request):
    lion_posts = Lion_Post.objects.all
    positions = Position.objects.all
    return render(request, 'gaeul.html', {'lion_posts':lion_posts, 'positions': positions})