from django.db import models

# Create your models here.
# class Lion_Post(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=50)
#     content = models.TextField()
    
#     def __str__(req):
#         return req.content
    
class Ex_Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    only_time = models.TimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Nowon(models.Model):
    food = models.CharField(max_length=100)
    cafe = models.CharField(max_length=100)
    mountain = models.CharField(max_length=100)
    store = models.CharField(max_length=100)
    
    def __str__(seq):
        return seq.food
    
class Position(models.Model):
    pos = models.CharField(max_length=50)
    explanation = models.TextField()
    reason = models.TextField()
    
    def __str__(self):
        return self.pos
    