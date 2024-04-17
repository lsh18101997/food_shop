from django.db import models
from django.contrib.auth.models import User
from seller.models import Food

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=0)
