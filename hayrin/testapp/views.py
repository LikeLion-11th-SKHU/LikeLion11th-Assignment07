from django.shortcuts import render
from .models import hayrin_Post
from .models import main_Post


# Create your views here.
def main(request):
    main_posts = main_Post.objects.all()
    return render(request, 'main.html', {'main_posts': main_posts})


def hayrin(request):
    rin_posts = hayrin_Post.objects.all()
    return render(request, 'hayrin.html', {'rin_posts': rin_posts})
