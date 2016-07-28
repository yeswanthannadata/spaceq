from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(City)
admin.site.register(Spaces)
admin.site.register(Area)
admin.site.register(CoSpace)

class CitySpaceAdmin(admin.ModelAdmin):
    list_display = ["city","space"]
admin.site.register(CitySpaces,CitySpaceAdmin)

