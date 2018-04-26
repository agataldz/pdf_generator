from django.db import models


class Pdf (models.Model):
    word = models.CharField(max_length=32)
    text = models.TextField()
    number = models.IntegerField()
    date = models.DateField()
