from django.db import models


class Organization(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    contributor = None

    def __str__(self):
        return f'{self.name}'
