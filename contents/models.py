from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg    


class Content(models.Model):
    
    title = models.CharField(max_length=100)
    context = models.TextField(max_length=5000)
    rate = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    user = models.ManyToManyField(User)
    content = models.ManyToManyField(Content)
    rate = models.PositiveSmallIntegerField()





