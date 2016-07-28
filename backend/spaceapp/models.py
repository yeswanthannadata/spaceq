from __future__ import unicode_literals

from django.db import models

# Create your models here.

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city    = models.CharField(max_length=255, unique=True)
    city_aka = models.CharField(max_length=255, default='', blank=True)

    class Meta:
	db_table = u'city'
    def __unicode__(self):
	return self.city

class Spaces(models.Model):
    space_id = models.AutoField(primary_key=True)
    space    = models.CharField(max_length=255, unique=True)
    fav_icon = models.CharField(max_length=255, default='', blank=True)
    logo     = models.CharField(max_length=255, default='', blank=True)
    image    = models.CharField(max_length=255, default='', blank=True)
    youtube_page = models.CharField(max_length=255, default='', blank=True)
    web      = models.CharField(max_length=255, default='', blank=True)
    fb_page  = models.CharField(max_length=255, default='', blank=True)
    blog_link= models.CharField(max_length=255, default='', blank=True)
    twitter_link = models.CharField(max_length=255, default='', blank=True)

    class Meta:
	db_table = u'space'
    def __unicode__(self):
	return self.space

class CitySpaces(models.Model):
    city_space_id = models.AutoField(primary_key=True)
    city          = models.ForeignKey(City, null=True)
    space         = models.ForeignKey(Spaces, null=True)

    class Meta:
	db_table = u'city_space'

class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    city_id = models.ForeignKey(City, null=True)
    area    = models.CharField(max_length=255, default='')

    class Meta:
	db_table = u'area'
	unique_together = (("city_id","area"),)
    def __unicode__(self):
	return self.area

class CoSpace(models.Model):
    co_space_id = models.AutoField(primary_key=True)
    city_id     = models.ForeignKey(City, null=True)
    area_id     = models.ForeignKey(Area, null=True)
    space_id    = models.ForeignKey(Spaces, null=True)
    title       = models.CharField(max_length=255, default='')
    aka         = models.CharField(max_length=255, default='', blank=True)
    description = models.TextField(default=True, blank=True)
    google_map  = models.CharField(max_length=255, default='', blank=True)
    mail_id     = models.CharField(max_length=255, default='', blank=True)
    contact_no  = models.CharField(max_length=255, default='', blank=True)

    class Meta:
	db_table = u'cospace'
    def __unicode__(self):
	return self.title
