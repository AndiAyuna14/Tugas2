from logging.handlers import RotatingFileHandler
from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    release_date = models.BigIntegerField()
    review  = models.TextField()