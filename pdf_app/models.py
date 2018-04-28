from django.db import models


class Pdf (models.Model):
    word = models.CharField(max_length=32)
    text = models.TextField()
    number = models.IntegerField()
    date = models.DateField()
    file = models.FileField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)