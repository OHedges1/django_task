from django.shortcuts import render
from django.http import HttpResponse
from holidays.models import CountryCodes, Holidays
import requests

def index(request):
    return HttpResponse("hello, world. You're at the index.")

def retrieve_from_db(request, countryCode_str):
    entrys = Holidays.objects.filter(countryCode__countryCode = countryCode_str)
    country_name = CountryCodes.objects.filter(pk = countryCode_str)
    if not country_name:
        return HttpResponse('Country code not found')
    data = {'holidays': entrys, 'country_name': country_name[0].countryName}#country_name[0].countryName}
    return render(request, 'table_template.html', data)


def fetch_and_save(request):
    holidayFields = [f.name for f in Holidays._meta.get_fields()][1:] # slice to remove 'id'
    objs = CountryCodes.objects.all()
    for obj in objs:
        key = obj.pk
        responses = requests.get('https://date.nager.at/api/v3/NextPublicHolidays/{}'.format(key)).json()
        print('saving {}: holidays to database'.format(key))
        for response in responses:
            tmp = {key: response[key] for key in holidayFields}
            tmp['countryCode'] = obj
            newObj = Holidays(**tmp) # look at setattr()
            newObj.save()
    print('saving successful')


    return HttpResponse('saved')
