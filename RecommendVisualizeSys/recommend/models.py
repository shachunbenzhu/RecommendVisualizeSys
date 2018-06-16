from django.db import models
from django.contrib import admin

# Create your models here.
class RecommendPost(models.Model):
    surl = models.CharField(max_length=150)
    name = models.CharField(max_length = 150)
    thumbnail = models.ImageField()
    birthDate = models.DateField()
    description = models.CharField(max_length = 150)
    abstract = models.TextField()

class ScientistPostAdmin(admin.ModelAdmin):
    list_display = ('surl', 'name', 'thumbnail', 'birthDate', 'description', 'abstract')

admin.site.register(RecommendPost, ScientistPostAdmin)