from django.db import models

# create your models here

class Contact(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=250, blank=True)
    email = models.EmailField(blank=True)
    dob = models.DateField(blank=True)
    address = models.TextField(blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name