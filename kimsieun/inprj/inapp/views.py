from django.shortcuts import render
from .models import Ex_Post
# Create your views here.

def main(request):
    ex_posts = Ex_Post.objects.all
    return render(request, 'main.html', {'xe_posts': ex_posts})

