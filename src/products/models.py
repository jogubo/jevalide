from django.db import models


class Product(models.Model):

    name = models.CharField(
        max_length=128
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
