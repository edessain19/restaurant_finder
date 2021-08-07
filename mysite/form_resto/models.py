from django.db import models

# Create your models here.

class Request(models.Model):
	localisation = models.CharField(max_length=200)
	max_dist = models.IntegerField()
	price_range = models.IntegerField()
	attendees = models.CharField(max_length=200)
	# food