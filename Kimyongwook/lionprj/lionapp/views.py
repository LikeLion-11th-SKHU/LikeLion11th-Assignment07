from django.shortcuts import render
from .models import Lion_Post
from .models import Ex_Post
import lionapp.views # lionapp에 있는 views를 가져와서 사용
# Create your views here.

def main(request): # request가 들어왔을 때 Template을 넘겨주는 함수
    lion_posts = Lion_Post.objects.all()
    return render(request, 'main.html' , {'lion_posts' : lion_posts})

def Yongwook(request): # request시 Template에 해당하는 html을 브라우저에 보여줌
    ex_posts = Ex_Post.objects.all() 
    return render(request, 'Yongwook.html' , {'ex_posts' : ex_posts})