from django.shortcuts import render
from .models import rin_Post
from .models import test_Post

# Create your views here.

def main(request):
    main_post = rin_Post.objects.all
    return render(request,'main.html' , {'main_posts': main_post})
def hayrin(request):
    hayrin_post = test_Post.objects.all
    return render(request,'hayrin.html' , {'hayrin_post': hayrin_post} )