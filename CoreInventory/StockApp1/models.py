from django.db import models

class Stock(models.Model):
    product = models.CharField(max_length=255)
    per_unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    on_hand = models.IntegerField(default=0)
    free_to_use = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product} | On Hand: {self.on_hand} | Free: {self.free_to_use}"