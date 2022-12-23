from enum import _auto_null
from django.db import models


class Student(models.Model):
    name = models.CharField(unique=True, max_length=50)
    reg_date = models.DateField(auto_now=True)
