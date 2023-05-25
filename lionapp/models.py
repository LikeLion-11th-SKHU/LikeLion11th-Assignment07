from django.db import models

# Create your models here.
class Lion_Post(models.Model) :
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100) #길이제한 있는 문자열
    content = models.TextField() #길이 제한이 없는 문자열
    create_time = models.DateTimeField(auto_now_add=True) #데이터 생성시 현재 시간 자동저장
    updated_time = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
