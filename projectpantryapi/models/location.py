from django.db import models

class Location(models.Model):
    title = models.CharField(max_length=30)