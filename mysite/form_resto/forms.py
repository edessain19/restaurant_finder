from django import forms
from django.forms import ModelForm
from .models import Request

class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		fields = ['localisation', 
				'maximum_distance', 
				'price', 
				'Gilles',
				'Vince',
				'Sam',
				'Klaas',
				'Gaelle',
			]
