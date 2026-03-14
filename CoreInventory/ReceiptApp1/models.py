from django.db import models
from WarehouseApp.models import Warehouse


class Receipt(models.Model):

    STATUS_CHOICES = [
        ('ready', 'Ready'),
        ('in-progress', 'In Progress'),
    ]

    reference = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name='receipts'
    )

    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)

    contact = models.CharField(max_length=50)

    schedule_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ready'
    )

    def __str__(self):
        return f"Receipt {self.id} - {self.reference.w_name}"