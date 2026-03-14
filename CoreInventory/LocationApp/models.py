from django.db import models

# Create your models here.
from django.db import models

class Location(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-increment primary key
    district = models.CharField(max_length=255)  # Location name
    state = models.CharField(max_length=100)  # State name
    pincode = models.CharField(max_length=20)  # Pincode as string

    def __str__(self):
        return f"{self.district}, {self.state} ({self.pincode})"