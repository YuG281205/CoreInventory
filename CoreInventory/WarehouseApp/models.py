from django.db import models
from LocationApp.models import Location

class Warehouse(models.Model):
    w_id = models.AutoField(primary_key=True)
    w_name = models.CharField(max_length=255)
    w_location = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.w_name