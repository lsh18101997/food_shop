from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    price = models.IntegerField()
    description=models.TextField()
    image_url=models.URLField()
