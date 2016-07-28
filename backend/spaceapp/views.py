from django.shortcuts import render
from models import CitySpaces,City,Spaces
from django.http import HttpResponse
#from common.utils import getHttpResponse as HttpResponse
import json

# Create your views here.

def citySpace(request):
    city_space_obj = CitySpaces.objects.all()
    data = []
    for obj in city_space_obj:
	city  = str(obj.city)
	space = str(obj.space)
	aka = City.objects.filter(city=obj.city).values_list('city_aka')[0][0]
	fav_icon = Spaces.objects.filter(space=obj.space).values_list('fav_icon')[0][0]
	data.append({'city':city,'space':space, 'aka':aka, 'fav_icon':fav_icon})
    return HttpResponse(json.dumps(data),"application/json")

def detail(request, space):
    city_space_obj = CitySpaces.objects.all()
    for obj in city_space_obj:
	if str(space) == str(obj.space).lower():
    	    return HttpResponse("You're looking at space %s in city %s" % (space,str(obj.city)))
    return HttpResponse("Not a valid space and citty")
    
