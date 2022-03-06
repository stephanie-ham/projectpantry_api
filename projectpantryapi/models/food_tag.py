from django.db import models


class FoodTag(models.Model):
    food = models.ForeignKey(
        'Food', on_delete=models.CASCADE,
        related_name='food_tags'
    )
    tag = models.ForeignKey(
        'Tag', on_delete=models.CASCADE,
        related_name='food_tags'
    )
    