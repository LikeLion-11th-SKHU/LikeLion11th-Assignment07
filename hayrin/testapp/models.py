from django.db import models

# Create your models here.

class hayrin_Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    only_time = models.TimeField

    def __str__(self):
        return self.title

class main_Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    only_time = models.TimeField

    def __str__(self):
        return self.title