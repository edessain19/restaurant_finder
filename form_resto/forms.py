from django import forms
from django.forms import ModelForm
from .models import Request

class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		fields = ['localisation',
				'distance', 
				'price', 
				'language_of_query',
				'Gilles',
				'Vince',
				'Sam',
				'Klaas',
				'Gaelle',
			]
