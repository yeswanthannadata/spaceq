from django.conf.urls import include, url 
from django.contrib import admin

urlpatterns = [ 
    url('^city_spaces','spaceapp.views.citySpace',name="city_space"),
    url(r'^(?P<space>\w+)/', 'spaceapp.views.detail', name='detail'),
]
