from django.db import models
# Create your models here.

class RSS(models.Model):
    description = models.CharField(max_length=200)
    time = models.TimeField(auto_created=True)

class NEWS(models.Model):
    rss = models.ManyToManyField(RSS, related_name='News',blank=True)