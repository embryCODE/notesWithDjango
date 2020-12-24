from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'{self.title}'
