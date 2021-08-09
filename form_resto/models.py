from django.db import models

# Create your models here.

PRICE_RANGE =(
    ("1", "less than 10€"),
    ("2", "between 11€ and 30€"),
    ("3", "between 31€ and 60€"),
    ("4", "over 61€"),
)
LANGUAGE = (
	("fr", "Français"),
	("en", "English"),
	("nl", "Dutch"),
)

class Request(models.Model):
	localisation = models.CharField(max_length=200)
	distance = models.IntegerField(default=1, help_text="in Km")
	price = models.CharField(default="" ,max_length=1, choices=PRICE_RANGE)
	language_of_query = models.CharField(default="", max_length=1, choices=LANGUAGE)
	Gilles = models.BooleanField(default=None)
	Vince = models.BooleanField(default=None)
	Sam = models.BooleanField(default=None)
	Klaas = models.BooleanField(default=None)
	Gaelle = models.BooleanField(default=None)