from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)  # Assuming contact is a name or info

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
