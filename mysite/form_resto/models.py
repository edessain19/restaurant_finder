from django.db import models

# Create your models here.

PRICE_RANGE =(
    ("1", "less than 10€"),
    ("2", "between 11€ and 30€"),
    ("3", "between 31€ and 60€"),
    ("4", "over 61€"),
)

class Request(models.Model):
	localisation = models.CharField(max_length=200)
	max_dist = models.IntegerField()
	price = models.CharField(max_length=1, choices=PRICE_RANGE)
	Gilles = models.BooleanField()
	Vince = models.BooleanField()
	Sam = models.BooleanField()
	Klaas = models.BooleanField()
	Gaelle = models.BooleanField()