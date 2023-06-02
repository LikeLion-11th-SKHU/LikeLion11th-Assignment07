from django.db import models

# Create your models here.

class Lion_Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    only_time = models.TimeField(blank=True)

    def __str__(self):
        return self.title
    
class Hometown(models.Model):
    home = models.CharField(max_length=100)
    river = models.CharField(max_length=100)
    food = models.CharField(max_length=100)

    def __str__(self):
        return self.home
    
class Position(models.Model):
    pos = models.CharField(max_length=100)
    explanation = models.TextField()
    reason = models.TextField()
    
    def __str__(self):
        return self.pos