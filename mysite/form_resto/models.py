from django.db import models

# Create your models here.

ATTENDEES_CHOICES =(
    ("1", "Gilles"),
    ("2", "Vince"),
    ("3", "Sam"),
    ("4", "Klaas"),
    ("5", "Gaelle"),
)

class Request(models.Model):
	localisation = models.CharField(max_length=200)
	max_dist = models.IntegerField()
	price_range = models.IntegerField()
	attendees = models.MultiSelectField(choices = ATTENDEES_CHOICES)
	# food