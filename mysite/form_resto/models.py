from django.db import models

# Create your models here.



def validate_distance(value):
    if value < 0 or value > 45:
        raise ValidationError(
            _('Insert a value smaller than 45 km'),
            params={'value': value},
        )

class Request(models.Model):
	localisation = models.CharField(max_length=200)
	max_dist = models.IntegerField(validators=[validate_distance])
	price = models.CharField(max_length=1, choices=[1,2,3,4,5])
	Gilles = models.BooleanField()
	Vince = models.BooleanField()
	Sam = models.BooleanField()
	Klaas = models.BooleanField()
	Gaelle = models.BooleanField()