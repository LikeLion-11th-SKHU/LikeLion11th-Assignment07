from django.contrib import admin
# from .models import Lion_Post
from assignmentapp.models import Lion_Post
from assignmentapp.models import Hometown
from assignmentapp.models import Position

# Register your models here.

admin.site.register(Lion_Post)
admin.site.register(Hometown)
admin.site.register(Position)
