from django.db import models

class Command(models.Model):
    command_name = models.CharField(max_length=255)
