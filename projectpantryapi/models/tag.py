from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    label = models.CharField(max_length=10)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='tags'
    )
    