from __future__ import unicode_literals

from django.db import models


class Patient(models.Model):

    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
