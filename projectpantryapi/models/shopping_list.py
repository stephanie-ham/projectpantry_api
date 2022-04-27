from django.db import models
from django.contrib.auth.models import User

class ShoppingList(models.Model):
    list_owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='safe_food'
    )
    food = models.ForeignKey(
        'Food', on_delete=models.CASCADE,
        related_name='safe_food'
    )
    