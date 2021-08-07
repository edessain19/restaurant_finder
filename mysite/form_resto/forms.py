from django import forms
from django.forms import ModelForm
from .models import Request


class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		fields = ['localisation', 
				'max_dist', 
				'price_range', 
				'attendees',
			]

# class RequestForm(forms.Form):
# 	localisation = forms.CharField(max_length=200)
# 	max_dist = forms.IntegerField()
# 	price_range = forms.IntegerField()
# 	attendees = forms.CharField(max_length=200)