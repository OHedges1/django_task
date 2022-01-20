from django.contrib import admin

# Register your models here.
from .models import CountryCodes, Holidays

admin.site.register(CountryCodes)
admin.site.register(Holidays)
