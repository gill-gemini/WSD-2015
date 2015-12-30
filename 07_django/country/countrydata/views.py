from django.http import Http404,HttpResponse,HttpRequest
from django.shortcuts import render_to_response, get_object_or_404
import json
from django.core import serializers
#from django.utils import simplejson as json

from .models import Continent, Country



def continent_json(request, continent_code):
    """ Write your answer in 7.2 here."""
    continent = get_object_or_404(Continent, code = continent_code)
    countries = Country.objects.all()
    cont_countries = {}
    for country in countries:
        if country.continent.code == continent_code:
            cont_countries[country.code] = country.name
            #print(country.name)
    json_dump = json.dumps(cont_countries)#, sort_keys=True)#, indent=2 * ' ')

    callback =request.GET.get("callback")
    if(callback):
        json_dump = '%s(%s)' % (callback, json_dump)

    return HttpResponse(json_dump, content_type='application/json; charset=utf-8')
    """if Continent.objects.get(code = continent_code):
        continentdata={}
        data =  Continent.objects.get(code__exact=continent_code)
        code1=data.code
        country=Country.objects.all()
        print(country)
        #country={}
        #continentdata=country
        for cont in country:
            print ("--------")
            if code1==cont.continent:
                print (cont.code)

                continentdata[cont.code]=cont.name
        continentdata=json.dumps(continentdata)
return HttpResponse(continentdata, content_type='application/json')
        """




        #print (data.code)




    #raise Http404("Not implemented")


def country_json(request, continent_code, country_code):
    """ Write your answer in 7.2 here. """
    #raise Http404("Not implemented")
    country = get_object_or_404(Country, code = country_code)
    if country.continent.code != continent_code:
        raise Http404
    json_dump = json.dumps({"area" : country.area, "population" : country.population, "capital" : country.capital})#, sort_keys=True)#, indent=2 * ' ')

    callback =request.GET.get("callback")
    if(callback):
        json_dump = '%s(%s)' % (callback, json_dump)



    return HttpResponse(json_dump,  content_type='application/json; charset=utf-8')
