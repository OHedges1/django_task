from django.shortcuts import render
from django.http import HttpResponse
from holidays.models import CountryCodes, Holidays
import requests

def index(request):
    return HttpResponse("hello, world. You're at the index.")

def retrive_from_db():
    ...

def fetch_and_save(request):
    holidayFields = [f.name for f in Holidays._meta.get_fields()][1:] # slice to remove 'id'
    objs = CountryCodes.objects.all()

    for obj in objs:
        key = obj.pk
        responses = requests.get('https://date.nager.at/api/v3/NextPublicHolidays/{}'.format(key)).json()

        for response in responses:
            tmp = {key: response[key] for key in holidayFields}
            tmp['countryCode'] = obj
            newObj = Holidays(**tmp)
            newObj.save()



    return HttpResponse('saved')
