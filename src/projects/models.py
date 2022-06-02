from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

    name = models.CharField(
        max_length=128
    )
    description = models.TextField(
        max_length=2048,
        blank=True
    )
    deadline = models.DateField()
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.name}'
