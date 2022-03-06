from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=40)
    location = models.ForeignKey(
        'Location', on_delete=models.CASCADE,
        related_name='foods'
    )
    quantity = models.ForeignKey(
        'Quantity', on_delete=models.CASCADE,
        related_name='foods'
    )
    image_path = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='foods'
    )
    tags = models.ManyToManyField(
        'Tag', through='FoodTag', related_name='foods'
    )
    safe_food = models.ManyToManyField(
        User, through='SafeList', related_name='safe_list'
    )
    