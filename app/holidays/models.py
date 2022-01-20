from django.db import models

# Create your models here.
class CountryCodes(models.Model):
    countryCode = models.CharField(max_length=10, primary_key=True)
    countryName = models.CharField(max_length=30)

class Holidays(models.Model):
    countryCode = models.ForeignKey(CountryCodes, on_delete=models.CASCADE)
    date = models.DateField()
    localName = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
