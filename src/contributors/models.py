from django.db import models
from django.contrib.auth.models import User

from organizations.models import Organization


class Contributor(models.Model):

    ROLES = [
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Production manager'),
        ('ART_DIRECTOR', 'Art Director'),
        ('PHOTOGRAPHER', 'Photographer'),
        ('RETOUCHER', 'Retoucher'),
        ('LOGISTICS', 'Logistics'),
        ('CUSTOMER', 'Customer'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contributor'
    )
    role = models.CharField(
        max_length=12,
        choices=ROLES
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='contributors'
    )

    def __str__(self):
        return f'{self.organizations} - {self.user}'
