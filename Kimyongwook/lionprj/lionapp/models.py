from django.db import models

# Create your models here.
class Lion_Post(models.Model):
    user = models.ForeignKey('auth.User' , on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True) 
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(req):
        return req.title

class Ex_Post(models.Model):
    user = models.ForeignKey('auth.User' , on_delete=models.CASCADE) ## auth.user: django 내장 user 모델 / on_delete = models.CASCADE
    title = models.CharField(max_length=500) # 길이 제한이 있는 문자열
    content = models.TextField() # 길이 제한이 없는 문자열 / 성능저하 이슈
    create_time = models.DateTimeField(auto_now_add=True) # 데이터 생성시 현재 시간 자동저장
    updated_time = models.DateTimeField(auto_now=True) # 데이터 업데이트시 현재 시간 자동저장

    def __str__(self): # __str__ 문자열 변환
        return self.title # class Ex_Post의 title로 return
    