from django.db import models

class Meme(models.Model):
    topic = models.CharField(max_length=15)
    image_URL = models.URLField()
