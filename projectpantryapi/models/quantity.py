from django.db import models

class Quantity(models.Model):
    title = models.CharField(max_length=5)
    