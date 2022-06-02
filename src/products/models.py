from django.db import models

from projects.models import Project


class Product(models.Model):

    name = models.CharField(
        max_length=128
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL
    )
    product_code = models.CharField(
        max_length=13,
    )
    entry_shipping_date = models.DateField(blank=True)
    entry_receipt = models.DateField(blank=True)
    return_shipping_date = models.DateField(blank=True)
    return_deadline = models.DateField(blank=True)

    def __str__(self):
        return f'{self.name}'
