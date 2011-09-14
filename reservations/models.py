from django.db import models

class Room(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	building = models.ForeignKey('Building')
	occupancy = models.IntegerField()
	image = models.ImageField(upload_to="media/images/room_images", null=True)
	opening_time = models.TimeField()
	closing_time = models.TimeField()

	def __unicode__(self):
		return self.name

class Building(models.Model):
	name = models.CharField(max_length=40)
	description = models.TextField()
	location = models.CharField(max_length=50)
	latitude = models.FloatField(blank=True)
	longitude = models.FloatField(blank=True)

	def __unicode__(self):
		return self.name

class Reservation(models.Model):
	user = models.ForeignKey(User)		
